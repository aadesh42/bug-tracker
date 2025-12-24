from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base
from .enums import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), default=UserRole.TESTER)


class Bug(Base):
    __tablename__ = "bugs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(String(50), default="OPEN")
    priority = Column(String(50), default="MEDIUM")
    created_at = Column(DateTime, default=datetime.utcnow)

    created_by_id = Column(Integer, ForeignKey("users.id"))
    created_by = relationship("User")


class BugAuditLog(Base):
    __tablename__ = "bug_audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    bug_id = Column(Integer, ForeignKey("bugs.id"), nullable=False)
    old_status = Column(String(50))
    new_status = Column(String(50))
    changed_by_id = Column(Integer, ForeignKey("users.id"))
    changed_at = Column(DateTime, default=datetime.utcnow)

    bug = relationship("Bug")
    changed_by = relationship("User")
