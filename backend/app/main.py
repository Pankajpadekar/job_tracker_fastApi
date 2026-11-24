from fastapi import FastAPI
from app.core.config import settings 

app = FastAPI(title=settings.app_name)

@app.get("/home")
async def home():
    return {"message" : "Welcome to the Job Tracker API"}

@app.get("/health")
async def health():
    return {"status" : "ok"}