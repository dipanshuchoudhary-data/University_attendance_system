from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import SessionLocal
from models import User
from auth import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


# ---------------------------
# Dependency: DB session
# ---------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------
# REGISTER (Admin / Professor)
# ---------------------------
@router.post("/register")
def register_user(
    username: str,
    password: str,
    role: str,
    db: Session = Depends(get_db)
):
    try:
        if role not in ["admin", "professor"]:
            raise HTTPException(status_code=400, detail="Invalid role")

        existing = db.query(User).filter(User.username == username).first()
        if existing:
            raise HTTPException(status_code=400, detail="Username already exists")

        user = User(
            username=username,
            password=hash_password(password),
            role=role
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return {"message": f"{role} registered successfully"}

    except Exception as e:
        print("REGISTER ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))

# ---------------------------
# LOGIN
# ---------------------------
@router.post("/login")
def login_user(
    username: str,
    password: str,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    token = create_token({
        "sub": user.username,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user.role
    }
