from datetime import datetime

import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.constants.constants import *

from app.models import models
from app.database import engine

from app.routers import content, courses, section, users, file_upload, resources

models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESC,
    version=APP_VERSION,
    contact=APP_CONTACT,
    license_info=APP_LICENSE
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=origins,
    allow_headers=origins,
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users.router)

app.include_router(courses.router)

app.include_router(content.router)

app.include_router(section.router)

app.include_router(resources.router)

app.include_router(file_upload.router)

@app.get("/")
async def root():
    return {
        "status": "OK!",
        "app": "OeRMS",
        "date": datetime.now()
    }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')