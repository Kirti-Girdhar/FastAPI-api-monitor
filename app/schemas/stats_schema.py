from pydantic import BaseModel

class StatsResponse(BaseModel):
    endpoint_id: int
    total_checks: int
    success_rate: float
    avg_response_time: float

    class Config:
        from_attributes = True