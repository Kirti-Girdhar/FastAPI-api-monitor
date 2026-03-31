from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.stats_service import get_endpoint_stats

router=APIRouter(
    prefix="/stats",
    tags=['Stats']
)

@router.get("/endpoint/{endpoint_id}")
def endpoint_stats(endpoint_id: int, db: Session = Depends(get_db)):
    stats= get_endpoint_stats(endpoint_id,db)
    return stats