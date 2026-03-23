from sqlalchemy import Column, Integer, Float, Boolean,ForeignKey,DateTime
from app.database import Base
from datetime import datetime

class Check(Base):
    __tablename__="checks"

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer, ForeignKey("endpoints.id"))
    status_code = Column(Integer, nullable=True)
    response_time= Column(Float)
    success= Column(Boolean)
    checked_at = Column(DateTime, default=datetime.utcnow)