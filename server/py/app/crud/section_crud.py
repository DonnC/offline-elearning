from sqlalchemy.orm import Session
from app.constants.constants import FETCH_LIMIT

from app.models import models
from app.schemas import schema

def get_sections(db: Session, skip: int = 0, limit: int = FETCH_LIMIT):
    return db.query(models.Section).offset(skip).limit(limit).all()

def get_section(db: Session, section_id: int):
    return db.query(models.Section).filter(models.Section.id == section_id).first()

def get_section_by_id(db: Session, section_id: int):
    return db.query(models.Section).get(section_id)

def get_section_query(db: Session, section_id: int):
    return db.query(models.Section).filter(models.Section.id == section_id)

def get_section_by_title(db: Session, title: str):
    return db.query(models.Section).filter(models.Section.title == title).first()

def create_content_section(db: Session, section: schema.SectionCreate, course_content_id: int, editor: int):
    db_section = models.Section(**section.dict(), content_id=course_content_id, user_id=editor)
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section
