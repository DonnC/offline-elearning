from sqlalchemy.orm import Session
from app.constants.constants import FETCH_LIMIT

from app.models import models
from app.schemas import schema

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_course_by_id(db: Session, course_id: int):
    return db.query(models.Course).get(course_id)

def get_course_query(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id)

def get_courses(db: Session, skip: int = 0, limit: int = FETCH_LIMIT):
    return db.query(models.Course).offset(skip).limit(limit).all()

def get_course_by_name(db: Session, name: str):
    return db.query(models.Course).filter(models.Course.name == name).first()

def create_course(db: Session, course: schema.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course