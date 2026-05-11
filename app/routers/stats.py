from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users import User
from app.models.endpoint import Endpoint
from app.schemas.stats_schema import StatsResponse
from app.services.stats_service import get_endpoint_stats 
from app.utils.dependencies import get_current_user

router=APIRouter(
    prefix="/stats",
    tags=['Stats']
)

@router.get("/endpoint/{endpoint_id}", response_model=StatsResponse)
def endpoint_stats(endpoint_id: int, db: Session = Depends(get_db), current_user :User= Depends(get_current_user)):
    endpoint = db.query(Endpoint).filter(Endpoint.id == endpoint_id, Endpoint.user_id == current_user.id).first()
    if not endpoint:
        raise HTTPException(status_code=404, detail="Endpoint not found")
    stats= get_endpoint_stats(endpoint_id,db)
    return stats