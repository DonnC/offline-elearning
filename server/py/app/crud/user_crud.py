from sqlalchemy.orm import Session
from app.dependencies import hash_password

from app.models import models
from app.schemas import schema

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_query(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id)

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).get(user_id)

def get_admin_user(db: Session):
    # there should be only 1 admin user
    return db.query(models.User).filter(models.User.is_admin == True).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_user(db: Session, db_user: models.User):
    # handled by router
    pass

def create_user(db: Session, user: schema.UserCreate):
    _hashed_password = hash_password(user.password)
    
    db_user = models.User(
        name=user.name, 
        is_admin=user.is_admin,
        is_teacher=user.is_teacher,
        is_student=user.is_student,
        hashed_password=_hashed_password
    )
   
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user