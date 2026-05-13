import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from app.core.limiter import limiter

from app.database import Base, engine, SessionLocal
from app.routers import auth, endpoints, alerts, stats
from sqlalchemy import text

from app.scheduler.monitor_scheduler import start_scheduler,scheduler
from app.utils.logger import setup_logger

from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

# Initialize logger
logger = setup_logger()
logger.info("Application started")

# Initialize FastAPI app 
app = FastAPI(
    title="API Monitoring System",
    description="Production-style API monitoring backend using FastAPI",
    version="1.0.0"
)

allowed_origins = settings.allowed_origins.split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in allowed_origins],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Initialize rate limiter
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "detail": "Too many requests. Please try again later.",
        }
    )

# Create all tables
Base.metadata.create_all(bind=engine)

API_PREFIX = "/api/v1"
app.include_router(auth.router, prefix=API_PREFIX)
app.include_router(endpoints.router, prefix=API_PREFIX)
app.include_router(alerts.router, prefix=API_PREFIX)
app.include_router(stats.router, prefix=API_PREFIX)

@app.get("/")
async def root():
    return {"message": "API Monitor Service Running"}

@app.get("/health")
async def health_check():
    """Basic health check endpoint for container orchestration"""
    return {"status": "healthy", "service": "api-monitor"}

@app.get("/ready")
async def readiness_check():
    """Readiness check - verifies database connectivity"""
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        return {"status": "ready", "database": "connected"}
    except Exception as e:
        logger.error(f"Readiness check failed: {str(e)}")
        return JSONResponse(
            status_code=503,
            content={"status": "not ready", "error": "Database connection failed"}
        )
    finally:
        db.close()

@app.on_event("startup")
async def startup_event():
    logger.info("Starting scheduler...")
    if not scheduler.running:
        scheduler.start()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down scheduler...")
    if scheduler.running:
        scheduler.shutdown()