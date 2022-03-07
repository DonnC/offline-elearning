from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import  Session, select

from app.dependencies import get_db
from app.models import models

from app.schemas import schema
from app.crud import course_crud as crud

#from ..dependencies import get_token_header

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schema.Course)
async def create_course(course: schema.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_name(db, name=course.name)

    if db_course:
        raise HTTPException(status_code=400, detail="Course already registered")
    
    return crud.create_course(db=db, course=course)


@router.get("/", response_model=list[schema.Course])
async def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses


@router.get("/{course_id}", response_model=schema.Course)
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)

    if db_course is None:
    
        raise HTTPException(status_code=404, detail="course not found")
    
    return db_course


@router.patch("/{course_id}", response_model=schema.Course)
async def update_course(course_id: int, course: schema.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)

    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")

    updated_course_model = models.Course(**course.dict())
    
    updated_course = updated_course_model.copy(update=course.dict(exclude_unset=True))

    return crud.update_course(db, updated_course)