import time
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.check import Check
from app.core.cache import cache_store, CACHE_TTL

def get_endpoint_stats(endpoint_id :int , db: Session):

    cache_key= f'stats_{endpoint_id}'
    current_time= time.time()
    if cache_key in cache_store:
        cached_data = cache_store[cache_key]
        age= current_time - cached_data["timestamp"]

        # Cache still valid
        if age < CACHE_TTL:
            print("Returning cached stats")
            return cached_data["data"]

    checks = (
        db.query(Check)
        .filter(Check.endpoint_id == endpoint_id)
        .all()
    )
    # total_check= db.query(Check).filter(Check.endpoint_id== endpoint_id).count()
    total_check= len(checks)

    # success_check= db.query(Check).filter(Check.endpoint_id==endpoint_id,Check.success==True).count()
    success_check = len(
        [c for c in checks if c.success])
    
    # avg_response_time=db.query(func.avg(Check.response_time)).filter(Check.endpoint_id==endpoint_id).scalar()
    avg_response_time = 0

    if total_check > 0:
        avg_response_time = (
            sum(c.response_time for c in checks)
            / total_check
        )

    success_rate= 0
    if total_check > 0:
        success_rate=(
            success_check/total_check
        )*100

    avg_response_time=round(avg_response_time or 0,2)
    success_rate=round(success_rate,2)

    stats = {
        "endpoint_id": endpoint_id,
        "total_checks": total_check,
        "success_rate": success_rate,
        "success_checks": success_check,
        "failed_checks": total_check - success_check,
        "avg_response_time":avg_response_time
    }

    # Store In Cache
    cache_store[cache_key] = {
        "data": stats,
        "timestamp": current_time
    }

    print("Returning fresh stats")

    return stats