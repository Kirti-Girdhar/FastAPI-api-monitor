# Removed unused APIRouter import & added null check for curr_user to prevent returning None from get_current_user
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from app.models.users import User
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from app.utils.security import SECRET_KEY, ALGORITHM
from app.schemas.user import TokenData


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token:str=Depends(oauth2_scheme),db: Session= Depends(get_db)):
    try:
        # print(token)
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        mail=payload.get("sub")
        if mail is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        token_data=TokenData(email=mail)
        curr_user=db.query(User).filter(User.email== token_data.email).first()
        if curr_user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return curr_user