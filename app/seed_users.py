from sqlalchemy.orm import Session
from passlib.context import CryptContext
from database import SessionLocal
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def seed_users():
    db: Session = SessionLocal()

    users = [
        ("admin", "admin123", "ADMIN"),
        ("tester", "tester123", "TESTER"),
        ("dev", "dev123", "DEVELOPER"),
    ]

    for username, password, role in users:
        existing = db.query(User).filter(User.username == username).first()
        if not existing:
            user = User(
                username=username,
                password=pwd_context.hash(password),
                role=role
            )
            db.add(user)

    db.commit()
    db.close()
