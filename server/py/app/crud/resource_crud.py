from sqlalchemy.orm import Session
from app.constants.constants import FETCH_LIMIT

from app.models import models
from app.models.resource_types_enum import ResourceParent, ResourceTypeEnum
from app.schemas import schema

def get_resources(db: Session, skip: int = 0, limit: int = FETCH_LIMIT):
    return db.query(models.Resource).offset(skip).limit(limit).all()

def get_resource(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def get_resource_by_id(db: Session, resource_id: int):
    return db.query(models.Resource).get(resource_id)

def get_resource_query(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id)

def get_resource_by_type(db: Session, type: ResourceTypeEnum):
    return db.query(models.Resource).filter(models.Resource.type == type.value).all()

def get_section_resources(db: Session, section_id: int, type: ResourceTypeEnum = None):
    _filter_sec = models.Resource.section_id == section_id

    if type:
        return db.query(models.Resource).filter(models.Resource.section_id == section_id).filter(models.Resource.type == type.value).all()

    return db.query(models.Resource).filter(_filter_sec).all()

def get_course_resources(db: Session, course_id: int, type: ResourceTypeEnum = None):
    _filter_course = models.Resource.course_id == course_id

    if type:
        return db.query(models.Resource).filter(models.Resource.course_id == course_id).filter(models.Resource.type == type.value).all()

    return db.query(models.Resource).filter(_filter_course).all()


def get_resource_by_parent(db: Session, parent: ResourceParent):
    '''
    course | section
    '''
    return db.query(models.Resource).filter(models.Resource.belong_to == parent.value).all()


def create_course_resource(db: Session, resource: schema.ResourceCreate, course_id: int):
    '''
        can create a content resource
    '''
    
    db_resource = models.Resource(**resource.dict(), course_id=course_id)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def create_section_resource(db: Session, resource: schema.ResourceCreate, section_id: int):
    '''
        create a section resource
    '''
    db_resource = models.Resource(**resource.dict(), section_id=section_id)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource
