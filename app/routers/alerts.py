from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.alert import Alert
from app.models.endpoint import Endpoint
from app.models.users import User
from app.utils.dependencies import get_current_user

router=APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)

# 
@router.get("/")
def get_alerts(skip: int=0, limit:int=10,db:Session=Depends(get_db),current_user: User=Depends(get_current_user)):

    query = db.query(Alert).join(Endpoint).filter(Endpoint.user_id == current_user.id).order_by(Alert.created_at.desc())
    total = query.count()
    alerts = query.offset(skip).limit(limit).all()

    return{
        "total":total,
        "alerts":alerts
    }
    