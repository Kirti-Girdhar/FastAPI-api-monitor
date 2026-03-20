# Request/Response schemas with validation - EndpointCreate for input, EndpointResponse with id/user_id for output
from pydantic import BaseModel
from typing import Optional

class EndpointCreate(BaseModel):
    name: str
    url: str
    method: str
    check_interval: int

class EndpointResponse(EndpointCreate):
    id: int
    user_id: int
    
    class Config:
        from_attributes = True