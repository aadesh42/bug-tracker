from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine, get_db
from .models import Bug, BugAuditLog, User, Base
from .schemas import BugCreate, BugResponse, BugUpdateStatus
from .enums import BugStatus, UserRole
from .auth import router as auth_router
from .dependencies import get_current_user
from .permissions import require_roles

app = FastAPI()

app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

VALID_TRANSITIONS = {
    BugStatus.OPEN: {BugStatus.IN_PROGRESS},
    BugStatus.IN_PROGRESS: {BugStatus.FIXED, BugStatus.REOPENED},
    BugStatus.FIXED: {BugStatus.CLOSED, BugStatus.REOPENED},
    BugStatus.REOPENED: {BugStatus.IN_PROGRESS},
    BugStatus.CLOSED: set(),
}

# =========================
# ROUTES
# =========================

@app.post("/bugs", response_model=BugResponse)
def create_bug(
    bug: BugCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.TESTER, UserRole.ADMIN))
):
    new_bug = Bug(
        title=bug.title,
        description=bug.description,
        priority=bug.priority,
        created_by_id=current_user.id
    )
    db.add(new_bug)
    db.commit()
    db.refresh(new_bug)
    return new_bug


@app.patch("/bugs/{bug_id}/status", response_model=BugResponse)
def update_bug_status(
    bug_id: int,
    update: BugUpdateStatus,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.DEVELOPER, UserRole.ADMIN))
):
    bug = db.query(Bug).filter(Bug.id == bug_id).first()

    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")

    if update.status not in VALID_TRANSITIONS[bug.status]:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status transition from {bug.status} to {update.status}"
        )

    audit = BugAuditLog(
        bug_id=bug.id,
        old_status=bug.status,
        new_status=update.status,
        changed_by_id=current_user.id
    )

    bug.status = update.status

    db.add(audit)
    db.commit()
    db.refresh(bug)

    return bug


@app.get("/bugs/{bug_id}/audit")
def get_bug_audit(
    bug_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN))
):
    logs = (
        db.query(BugAuditLog)
        .filter(BugAuditLog.bug_id == bug_id)
        .all()
    )

    return [
        {
            "old_status": log.old_status,
            "new_status": log.new_status,
            "changed_at": log.changed_at,
            "changed_by": log.changed_by.username
        }
        for log in logs
    ]


@app.get("/bugs", response_model=list[BugResponse])
def list_bugs(db: Session = Depends(get_db)):
    return db.query(Bug).all()


@app.get("/")
def root():
    return {"message": "Bug Tracker API is running"}
