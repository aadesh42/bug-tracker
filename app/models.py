from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Enum,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base
from .enums import BugStatus, BugPriority, UserRole


# =========================
# USER MODEL
# =========================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    bugs_created = relationship("Bug", back_populates="created_by")
    audit_logs = relationship("BugAuditLog", back_populates="changed_by")


# =========================
# BUG MODEL
# =========================

class Bug(Base):
    __tablename__ = "bugs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(BugStatus), default=BugStatus.OPEN, nullable=False)
    priority = Column(Enum(BugPriority), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_by = relationship("User", back_populates="bugs_created")

    audit_logs = relationship("BugAuditLog", back_populates="bug")


# =========================
# BUG AUDIT LOG MODEL
# =========================

class BugAuditLog(Base):
    __tablename__ = "bug_audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    bug_id = Column(Integer, ForeignKey("bugs.id"), nullable=False)
    old_status = Column(Enum(BugStatus), nullable=False)
    new_status = Column(Enum(BugStatus), nullable=False)

    changed_at = Column(DateTime, default=datetime.utcnow)

    changed_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    bug = relationship("Bug", back_populates="audit_logs")
    changed_by = relationship("User", back_populates="audit_logs")
