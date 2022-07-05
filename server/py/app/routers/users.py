from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import  Session, select
from app.constants.constants import FETCH_LIMIT

from app.dependencies import get_db, hash_password
from app.models import models

from app.schemas import schema
from app.crud import user_crud as crud

#from ..dependencies import get_token_header

router = APIRouter(
    prefix="/users",
    tags=["users"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/register", response_model=schema.User)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)

    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
        

    return crud.create_user(db=db, user=user)

@router.post("/login", response_model=schema.User)
async def login_user(user: schema.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)

    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect name or password")

    hashed_pwd = hash_password(user.password)

    if not hashed_pwd == db_user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect name or password")

    return db_user

@router.get("/", response_model=List[schema.User])
async def read_users(skip: int = 0, limit: int = FETCH_LIMIT, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schema.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if db_user is None:
    
        raise HTTPException(status_code=404, detail="User not found")
    
    return db_user


@router.patch("/", response_model=schema.User)
async def update_user( user: schema.User, db: Session = Depends(get_db)):
    db_user = crud.get_user_query(db, user_id=user.id)

    if not db_user.first():
        raise HTTPException(status_code=404, detail="User not found")

    db_user.update(
        {
            "name": user.name,
            "is_admin": user.is_admin,
            "is_teacher": user.is_teacher,
            "is_student": user.is_student,
        }
    )

    db.commit()
    #db.refresh(db_user)

    return crud.get_user(db, user_id=user.id)

@router.delete("/{user_id}", response_model=schema.User)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_usr = crud.get_user_by_id(db, user_id=user_id)

    db.delete(db_usr)

    db.commit()

    return None