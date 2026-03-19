from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
import os

SECRET_KEY = os.getenv("SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_TIME = 60

pwd_context = CryptContext(schemes=["argon2","bcrypt"], deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(password:str, hashed_password:str):
    return pwd_context.verify(password,hashed_password)


def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)
    to_encode.update({"exp": expire})
    encoded=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded