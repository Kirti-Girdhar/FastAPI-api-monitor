# Endpoint model with relationship to User model - supports create, read, delete operations via REST API
from sqlalchemy import Column, Integer,String,ForeignKey
from app.database import Base

class Endpoint(Base):
    __tablename__= "endpoints"

    id=Column(Integer,primary_key=True)
    name=Column(String, nullable=False)
    url=Column(String, nullable=False)
    method=Column(String, nullable=False)
    check_interval=Column(Integer)

    user_id=Column(Integer, ForeignKey("users.id"))

