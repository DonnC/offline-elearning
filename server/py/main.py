from datetime import datetime

from fastapi import  FastAPI

from app.config import create_db_and_tables

from app.routers import course_topic, heroes, teams, course_topic_content

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(heroes.router)

app.include_router(teams.router)

app.include_router(course_topic.router)

app.include_router(course_topic_content.router)

@app.get("/")
async def root():
    return {
        "status": "OK!",
        "app": "OeRMS",
        "date": datetime.now()
    }