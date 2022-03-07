from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import  Session, select

from app.dependencies import get_db
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

@router.post("/", response_model=schema.User)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=list[schema.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schema.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if db_user is None:
    
        raise HTTPException(status_code=404, detail="User not found")
    
    return db_user


@router.patch("/{user_id}", response_model=schema.User)
async def update_user(user_id: int, user: schema.User, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user_model = models.User(**user.dict())
    
    updated_user = updated_user_model.copy(update=user.dict(exclude_unset=True))

    return crud.update_user(db, updated_user)