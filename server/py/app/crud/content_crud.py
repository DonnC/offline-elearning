from sqlalchemy.orm import Session

from app.models import models
from app.schemas import schema

def get_contents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Content).offset(skip).limit(limit).all()


def get_content_by_topic(db: Session, topic: str):
    return db.query(models.Content).filter(models.Content.topic == topic).first()

def get_content(db: Session, content_id: int):
    return db.query(models.Content).filter(models.Content.id == content_id).first()

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