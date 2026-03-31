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
def get_alerts(db:Session=Depends(get_db),current_user: User=Depends(get_current_user)):

    alerts=db.query(Alert).join(Endpoint).filter(Endpoint.user_id == current_user.id).all()
    return alerts
