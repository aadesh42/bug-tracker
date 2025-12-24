from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from .enums import BugStatus
from .enums import UserRole

class BugCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "MEDIUM"

class BugUpdateStatus(BaseModel):
    status: BugStatus

class BugResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: BugStatus
    priority: str
    created_at: datetime

    class Config:
        orm_mode = True
class BugAuditResponse(BaseModel):
    old_status: str
    new_status: str
    changed_at: datetime
    changed_by: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.TESTER

class UserResponse(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Config:
        from_attributes = True
