from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.database import SessionLocal
from app.models.endpoint import Endpoint
from app.services.monitoring_service import check_endpoint

scheduler = AsyncIOScheduler()

async def run_monitoring():
    db= SessionLocal()
    try:
        endpoints= db.query(Endpoint).all()
        for endpoint in endpoints:
            await check_endpoint(endpoint, db)
    finally:
        db.close()
    
def start_scheduler():
    scheduler.add_job(run_monitoring,
                      "interval",
                      seconds=60)
    scheduler.start()