from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import users
from app.utils.security import verify_password, hash_password, create_access_token
from app.schemas import user
from ..database import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/register")
def register(user_data:user.UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(users.User).filter(users.User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    hashed=hash_password(user_data.password)

    new_user= users.User(
        email= user_data.email,
        hashed_password=hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

@router.post("/login", response_model=user.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    db_user =db.query(users.User).filter(users.User.email== form_data.username).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid Credentials")
    
    if not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid Credentials")
    
    token=create_access_token(data={"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}