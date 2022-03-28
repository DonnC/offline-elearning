from sqlalchemy.orm import Session
from app.constants.constants import FETCH_LIMIT

from app.models import models
from app.schemas import schema

def get_contents(db: Session, skip: int = 0, limit: int = FETCH_LIMIT, course_id: int=None):
    if course_id:
        return db.query(models.Content).filter(models.Content.course_id == course_id).offset(skip).limit(limit).all()

    return db.query(models.Content).offset(skip).limit(limit).all()

def get_content_by_topic(db: Session, topic: str):
    return db.query(models.Content).filter(models.Content.topic == topic).first()

def get_content(db: Session, content_id: int):
    return db.query(models.Content).filter(models.Content.id == content_id).first()

def get_content_by_id(db: Session, content_id: int):
    return db.query(models.Content).get(content_id)

def get_content_query(db: Session, content_id: int):
    return db.query(models.Content).filter(models.Content.id == content_id)

def get_content_query_by_id(db: Session, content_id: int):
    return db.query(models.Content).get(content_id)


def create_course_content(db: Session, content: schema.ContentCreate, course_id: int):
    db_content = models.Content(**content.dict(), course_id=course_id)
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content

def update_content(db: Session, content: schema.Content):
    db_content = models.Content(**content.dict())
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content