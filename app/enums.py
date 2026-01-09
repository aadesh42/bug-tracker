from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    TESTER = "TESTER"
    DEVELOPER = "DEVELOPER"


class BugStatus(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    FIXED = "FIXED"
    REOPENED = "REOPENED"
    CLOSED = "CLOSED"


class BugPriority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

