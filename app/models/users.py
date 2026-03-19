from ..database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime   

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password=Column(String)
    created_at= Column(DateTime,nullable=False,default=datetime.utcnow)

