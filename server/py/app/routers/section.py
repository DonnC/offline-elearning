from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import  Session, select

from app.dependencies import get_db
from app.models import models

from app.schemas import schema
from app.crud import section_crud as crud

#from ..dependencies import get_token_header

router = APIRouter(
    prefix="/sections",
    tags=["sections"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/{course_content_id}", response_model=schema.Section)
async def create_section(course_content_id: int, section: schema.SectionCreate, db: Session = Depends(get_db)):
    db_section = crud.get_section_by_title(db, title=section.title)

    if db_section:
        raise HTTPException(status_code=400, detail="Section already exists")
    
    return crud.create_content_section(db=db, section=section, course_content_id=course_content_id)

@router.get("/", response_model=list[schema.Section])
async def read_sections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sections = crud.get_sections(db, skip=skip, limit=limit)
    return sections


@router.get("/{section_id}", response_model=schema.Section)
async def read_section(section_id: int, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, section_id=section_id)

    if db_section is None:
    
        raise HTTPException(status_code=404, detail="section not found")
    
    return db_section


@router.patch("/{section_id}", response_model=schema.Section)
async def update_section(section_id: int, section: schema.Section, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, section_id=section_id)

    if db_section is None:
        raise HTTPException(status_code=404, detail="section not found")

    updated_section_model = models.Section(**section.dict())
    
    updated_section = updated_section_model.copy(update=section.dict(exclude_unset=True))

    return crud.update_section(db, updated_section)