# Request/Response schemas with validation - EndpointCreate for input, EndpointResponse with id/user_id for output
from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional,Literal


class EndpointCreate(BaseModel):
    name: str
    url: HttpUrl
    method: Literal["GET", "POST"]
    check_interval: int

class EndpointResponse(EndpointCreate):
    id: int
    user_id: int
    
    class Config:
        from_attributes = True

class EndpointResult(BaseModel):
    id: int
    name: str
    url: HttpUrl
    method: str
    check_interval: int
    created_at: datetime
# fastAPI can't convert sqlalchemy object to json, with it, it can automatically convert 
    class Config:
        from_attributes = True