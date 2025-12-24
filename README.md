# 🐞 Bug Tracker API (FastAPI)

A production-style Bug Tracking System built with FastAPI, SQLAlchemy, and JWT authentication.

## 🚀 Features
- User registration & login (JWT)
- Role-based access control (Admin / Developer / Tester)
- Bug lifecycle management with enforced state transitions
- Immutable audit logs for compliance & traceability
- SQLite database with SQLAlchemy ORM
- Swagger/OpenAPI documentation

## 🧱 Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)
- Pydantic v2

## 🔐 Roles
- **Tester**: Create bugs
- **Developer**: Update bug status
- **Admin**: Full access, audit logs

## ▶️ Run Locally
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
