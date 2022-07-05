from typing import Optional, List, Union
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import  Session, select
from app.constants.constants import FETCH_LIMIT

from app.dependencies import get_db
from app.models import models

from app.schemas import schema
from app.crud import content_crud as crud, course_crud as ccrud

#from ..dependencies import get_token_header

router = APIRouter(
    prefix="/contents",
    tags=["contents"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/{course_id}", response_model=schema.Content)
async def create_content(course_id: int, content: schema.ContentCreate, db: Session = Depends(get_db)):
    # first check if content is available
    course_ = ccrud.get_course(db, course_id=course_id)

    if not course_:
        raise HTTPException(status_code=400, detail="no course found matching given id")

    db_content = crud.get_content_by_topic(db, topic=content.topic)

    if db_content:
        raise HTTPException(status_code=400, detail="Content already exists")
    
    return crud.create_course_content(db=db, content=content, course_id=course_id)


@router.get("/", response_model=List[schema.Content])
async def read_contents(course_id: Optional[int] = None, skip: int = 0, limit: int = FETCH_LIMIT, db: Session = Depends(get_db)):
    contents = crud.get_contents(db, skip=skip, limit=limit, course_id=course_id)
    return contents


@router.get("/{content_id}", response_model=schema.Content)
async def read_content(content_id: int, db: Session = Depends(get_db)):
    db_content = crud.get_content(db, content_id=content_id)

    if db_content is None:
    
        raise HTTPException(status_code=404, detail="Content not found")
    
    return db_content

@router.patch("/", response_model=schema.Content)
async def update_content( content: schema.Content, db: Session = Depends(get_db)):
    course_ = ccrud.get_course(db, course_id=content.course_id)

    if not course_:
        raise HTTPException(status_code=400, detail="no course found matching given id")

    db_content = crud.get_content_query(db, content_id=content.id)

    if not db_content.first():
        raise HTTPException(status_code=404, detail="Content not found")

    db_content.update(
        {
            "topic": content.topic,
            "description": content.description,
        }
    )

    db.commit()

    return crud.get_content(db, content_id=content.id)

@router.delete("/{content_id}")
async def delete_content(content_id: int, db: Session = Depends(get_db)):
    db_content_ = crud.get_content(db, content_id=content_id)

    if db_content_ is None:
        raise HTTPException(status_code=404, detail="content not found")

    db_content = crud.get_content_query_by_id(db, content_id=content_id)

    db.delete(db_content)

    db.commit()

    return None