from datetime import datetime



from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.models import models
from app.database import engine

from app.routers import content, courses, section, users, file_upload

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(file_upload.router)

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