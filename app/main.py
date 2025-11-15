# app/main.py
from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers import users

# Create tables if not exist (simple approach for this assignment)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure User FastAPI App",
    version="1.0.0",
)

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "FastAPI Secure User App is running"}
