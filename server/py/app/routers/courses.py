from typing import Optional, Union, List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import  Session
from app.constants.constants import FETCH_LIMIT

from app.dependencies import get_db
from app.models.grades_enums import GradeEnum

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
async def create_course(course: schema.CourseCreate,  form: GradeEnum, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_name_form(db, name=course.name, form=form.value)

    if db_course:
        raise HTTPException(status_code=400, detail="Course already registered")

    course.form = form.value
    
    return crud.create_course(db=db, course=course)

@router.get("/", response_model=List[schema.Course])
async def read_courses(form: Optional[GradeEnum] = None, skip: int = 0, limit: int = FETCH_LIMIT, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit, form=form)
    return courses

@router.get("/{course_id}", response_model=schema.Course)
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)

    if db_course is None:
    
        raise HTTPException(status_code=404, detail="course not found")
    
    return db_course

@router.patch("/", response_model=schema.Course)
async def update_course(course: schema.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course_query(db, course_id=course.id)

    if not db_course.first():
        raise HTTPException(status_code=404, detail="course not found")

    db_course.update(
        {
            "form": course.form,
            "name": course.name,
            "description": course.description,
            "synopsis": course.synopsis,
        }
    )

    db.commit()

    return crud.get_course(db, course_id=course.id)

@router.delete("/{course_id}")
async def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)

    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")

    db_c = crud.get_course_by_id(db, course_id=course_id)

    db.delete(db_c)

    db.commit()

    return None