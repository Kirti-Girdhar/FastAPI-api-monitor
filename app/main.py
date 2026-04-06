from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, endpoints, alerts, stats
from app.scheduler.monitor_scheduler import start_scheduler,scheduler
from app.utils.logger import setup_logger

# Initialize logger
logger = setup_logger()
logger.info("Application started")

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Starting scheduler...")
    start_scheduler()


app.include_router(auth.router)
app.include_router(endpoints.router)
app.include_router(alerts.router)
app.include_router(stats.router)

@app.get("/")
async def root():
    return {"message": "Hello World"} 

# @app.on_event("shutdown")
# async def shutdown_event():
#     print("Shutting down scheduler...")
#     scheduler.shutdown()