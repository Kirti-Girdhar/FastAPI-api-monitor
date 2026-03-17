from ..database import Base
from sqlalchemy import Column, Integer, String
from datetime import datetime   

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password=Column(String)
    created_at= Column(datetime,nullable=False,default=datetime.utcnow)

    