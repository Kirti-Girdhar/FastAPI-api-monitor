from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.database import SessionLocal
from app.models.endpoint import Endpoint
from app.services.monitoring_service import check_endpoint
import logging

logger = logging.getLogger(__name__)
scheduler = AsyncIOScheduler()

async def run_monitoring():
    db = SessionLocal()
    try:
        endpoints= db.query(Endpoint).all()
        for endpoint in endpoints:
            logger.info(f"Checking endpoint: {endpoint.url}")
            await check_endpoint(endpoint, db)
        logger.info("Monitoring cycle completed successfully")
    except Exception as e:
        logger.error(f"Error during monitoring: {str(e)}", exc_info=True)
    finally:
        db.close()
    
def start_scheduler():
    scheduler.add_job(run_monitoring,
                      "interval",
                      seconds=60)
    scheduler.start()