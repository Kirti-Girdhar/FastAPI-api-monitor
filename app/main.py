from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, endpoints
from app import models

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(endpoints.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}