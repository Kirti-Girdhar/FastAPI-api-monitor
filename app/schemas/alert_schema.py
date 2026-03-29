from pydantic import BaseModel
from datetime import datetime

class AlertResponse(BaseModel):
    id: int 
    endpoint_id:int
    message:str
    created_at:datetime

    class Config:
        from_attributes = True