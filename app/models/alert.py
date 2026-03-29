from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.database import Base

class Alert(Base):
    __tablename__ = "alerts"
    
    id= Column(Integer, primary_key=True, index=True)
    endpoint_id= Column(Integer,ForeignKey("endpoints.id"))
    message= Column(String)
    created_at= Column(DateTime,default=datetime.utcnow)