from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.check import Check

def get_endpoint_stats(endpoint_id :int , db: Session):
    total_check= db.query(Check).filter(Check.endpoint_id== endpoint_id).count()

    success_check= db.query(Check).filter(Check.endpoint_id==endpoint_id,Check.success==True).count()
    
    avg_response_time=db.query(func.avg(Check.response_time)).filter(Check.endpoint_id==endpoint_id).scalar()

    success_rate= 0
    if total_check > 0:
        success_rate=(
            success_check/total_check
        )*100

    avg_response_time=round(avg_response_time or 0,2)
    success_rate=round(success_rate,2)

    return{"endpoint_id":endpoint_id,
           "total_checks":total_check,
           "success_rate":success_rate,
           "avg_response_time":avg_response_time}