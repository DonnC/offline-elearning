from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import  Session, select

from app.dependencies import get_db
from app.models import models

from app.schemas import schema
from app.crud import content_crud as crud

#from ..dependencies import get_token_header

router = APIRouter(
    prefix="/contents",
    tags=["contents"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/{course_id}", response_model=schema.Content)
async def create_content(course_id: int, content: schema.ContentCreate, db: Session = Depends(get_db)):
    db_content = crud.get_content_by_topic(db, topic=content.topic)

    if db_content:
        raise HTTPException(status_code=400, detail="Content already exists")
    
    return crud.create_course_content(db=db, content=content, course_id=course_id)


@router.get("/", response_model=list[schema.Content])
async def read_contents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    Contents = crud.get_contents(db, skip=skip, limit=limit)
    return Contents


@router.get("/{content_id}", response_model=schema.Content)
async def read_content(content_id: int, db: Session = Depends(get_db)):
    db_content = crud.get_content(db, content_id=content_id)

    if db_content is None:
    
        raise HTTPException(status_code=404, detail="Content not found")
    
    return db_content


@router.patch("/{content_id}", response_model=schema.Content)
async def update_content(content_id: int, content: schema.Content, db: Session = Depends(get_db)):
    db_content = crud.get_content(db, content_id=content_id)

    if db_content is None:
        raise HTTPException(status_code=404, detail="Content not found")

    updated_content_model = models.Content(**content.dict())
    
    updated_content = updated_content_model.copy(update=content.dict(exclude_unset=True))

    return crud.update_content(db, updated_content)