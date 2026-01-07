from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import User
from .security import hash_password
from .enums import UserRole


def seed_users():
    db: Session = SessionLocal()

    users = [
        ("admin", "admin123", UserRole.ADMIN),
        ("tester", "tester123", UserRole.TESTER),
        ("dev", "dev123", UserRole.DEVELOPER),
    ]

    for username, password, role in users:
        existing = db.query(User).filter(User.username == username).first()
        if not existing:
            user = User(
                username=username,
                password_hash=hash_password(password),
                role=role
            )
            db.add(user)

    db.commit()
    db.close()
