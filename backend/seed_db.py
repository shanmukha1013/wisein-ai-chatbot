from database import engine, Base, SessionLocal
from models import User, Role
from auth import get_password_hash

print("Creating database tables...")
Base.metadata.create_all(bind=engine)

db = SessionLocal()
try:
    if not db.query(User).filter(User.username == "admin").first():
        admin = User(username="admin", hashed_password=get_password_hash("admin123"), role=Role.ADMIN)
        db.add(admin)
        print("Created admin user (admin/admin123)")
        
    if not db.query(User).filter(User.username == "user").first():
        user = User(username="user", hashed_password=get_password_hash("user123"), role=Role.USER)
        db.add(user)
        print("Created test user (user/user123)")
    db.commit()
except Exception as e:
    print(f"Error seeding database: {e}")
finally:
    db.close()
print("Done.")
