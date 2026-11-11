import logging
import secrets
from datetime import datetime, timedelta, timezone

import bcrypt
from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from jose import JWTError, jwt
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import config
from database import SessionLocal, get_db
from models import Role, User
from ratelimit import login_limiter

log = logging.getLogger("wisein.auth")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
COOKIE_NAME = "wisein_session"

router = APIRouter(prefix="/api/auth", tags=["auth"])


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except ValueError:
        return False


def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = {**data, "exp": datetime.now(timezone.utc) + expires_delta}
    return jwt.encode(to_encode, config.JWT_SECRET, algorithm=ALGORITHM)


def get_optional_user(request: Request, db: Session = Depends(get_db)) -> User | None:
    token = request.cookies.get(COOKIE_NAME)
    if not token:
        auth_header = request.headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header[7:]
    if not token:
        return None
    try:
        username = jwt.decode(token, config.JWT_SECRET, algorithms=[ALGORITHM]).get("sub")
    except JWTError:
        return None
    if not username:
        return None
    return db.query(User).filter(User.username == username).first()


def get_current_user(user: User | None = Depends(get_optional_user)) -> User:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Please log in.")
    return user


def get_current_staff(user: User = Depends(get_current_user)) -> User:
    if user.role not in (Role.ADMIN.value, Role.SUPPORT_AGENT.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough privileges")
    return user


def get_current_admin(user: User = Depends(get_current_user)) -> User:
    if user.role != Role.ADMIN.value:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough privileges")
    return user


def ensure_admin():
    """Make sure an admin account exists; sync its password with ADMIN_PASSWORD when that is set."""
    db = SessionLocal()
    try:
        admin = db.query(User).filter(User.username == "admin").first()
        if admin is None:
            password = config.ADMIN_PASSWORD or secrets.token_urlsafe(12)
            db.add(User(username="admin", hashed_password=get_password_hash(password), role=Role.ADMIN.value))
            try:
                db.commit()
            except IntegrityError:  # another instance created it at the same moment
                db.rollback()
                return
            if not config.ADMIN_PASSWORD:
                log.warning("Created admin user. Username: admin  Password: %s  (set ADMIN_PASSWORD in .env to choose your own)", password)
        elif config.ADMIN_PASSWORD and not verify_password(config.ADMIN_PASSWORD, admin.hashed_password):
            admin.hashed_password = get_password_hash(config.ADMIN_PASSWORD)
            db.commit()
            log.info("Admin password updated from ADMIN_PASSWORD.")
        elif not config.ADMIN_PASSWORD and verify_password("admin123", admin.hashed_password):
            log.warning("The admin account still uses the default password 'admin123'. Set ADMIN_PASSWORD in .env to change it.")
    finally:
        db.close()


class AuthRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(auth: AuthRequest, request: Request, response: Response, db: Session = Depends(get_db)):
    login_limiter.check(request)
    user = db.query(User).filter(User.username == auth.username).first()
    if not user or not verify_password(auth.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    token = create_access_token({"sub": user.username, "role": user.role}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    response.set_cookie(
        key=COOKIE_NAME, value=token, httponly=True, max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        samesite="lax", secure=config.COOKIE_SECURE,
    )
    return {"message": "Logged in successfully", "username": user.username, "role": user.role}


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(COOKIE_NAME)
    return {"message": "Logged out successfully"}


@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "role": current_user.role}
