from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.alert import Alert
from app.schemas.alert_schema import AlertResponse
from app.models.endpoint import Endpoint
from app.models.users import User
from app.utils.dependencies import get_current_user

router=APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)

# 
@router.get("/",response_model=list[AlertResponse])
def get_alerts(skip: int=0, limit: int = Query(10, le=50),db:Session=Depends(get_db),current_user: User=Depends(get_current_user)):

    query = db.query(Alert).join(Endpoint).filter(Endpoint.user_id == current_user.id).order_by(Alert.created_at.desc())
    total = query.count()
    alerts = query.offset(skip).limit(limit).all()

    return{
        "total":total,
        "alerts":alerts
    }
    