from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.models import models
from app.database import engine

from app.routers import content, courses, section, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

app.include_router(courses.router)

app.include_router(content.router)

app.include_router(section.router)

@app.get("/")
async def root():
    return {
        "status": "OK!",
        "app": "OeRMS",
        "date": datetime.now()
    }