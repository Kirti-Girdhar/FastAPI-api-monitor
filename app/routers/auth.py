from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import users
from app.utils.security import verify_password, hash_password, create_access_token
from app.schemas import user
from ..database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/register")
def register(user:user.UserCreate, db: Session = Depends(get_db)):
    hashed=hash_password(user.password)

    new_user= users.User(
        email= user.email,
        hashed_password=hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: user.UserLogin, db:Session=Depends(get_db)):
    db_user =db.query(users.User).filter(users.User.email== user.email).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid Credentials")
    
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid Credentials")
    
    token=create_access_token(data={"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}