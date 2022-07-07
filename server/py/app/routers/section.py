from fastapi import APIRouter, Depends, HTTPException
from typing import List, Union
from sqlmodel import  Session
from app.constants.constants import FETCH_LIMIT

from app.dependencies import get_db
from app.models import models

from app.schemas import schema
from app.crud import section_crud as crud, content_crud as ccrud, user_crud as ucrud

#from ..dependencies import get_token_header

router = APIRouter(
    prefix="/sections",
    tags=["sections"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/{course_content_id}/", response_model=schema.Section)
async def create_section(course_content_id: int, section: schema.SectionCreate, editor_id: int = None,  db: Session = Depends(get_db)):
    # first check if content is available
    content_content = ccrud.get_content(db, content_id=course_content_id)

    usr_id = editor_id

    if not content_content:
        raise HTTPException(status_code=400, detail="no course content found matching given id")

    # check if user is valid, if given
    if usr_id:
        editor = ucrud.get_user(db, user_id=usr_id)

        if not editor:
            # try taking admin
            admin_user = ucrud.get_admin_user(db)

            if not admin_user:
                raise HTTPException(status_code=400, detail="no staff member found matching given editor id")


            else:
                usr_id = admin_user.id
    
    else:
        admin_user = ucrud.get_admin_user(db)

        if not admin_user:
            raise HTTPException(status_code=400, detail="no admin staff member found matching given id")

        else:
            usr_id = admin_user.id

    # db_section = crud.get_section_by_title(db, title=section.title)

    # if db_section:
    #     raise HTTPException(status_code=400, detail="Section already exists")
    
    return crud.create_content_section(db=db, section=section, course_content_id=course_content_id, editor=usr_id)

@router.get("/", response_model=List[schema.Section])
async def read_sections(skip: int = 0, limit: int = FETCH_LIMIT, db: Session = Depends(get_db)):
    sections = crud.get_sections(db, skip=skip, limit=limit)
    return sections


@router.get("/{section_id}", response_model=schema.Section)
async def read_section(section_id: int, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, section_id=section_id)

    if db_section is None:
    
        raise HTTPException(status_code=404, detail="section not found")
    
    return db_section

@router.patch("/", response_model=schema.Section)
async def update_section(section: schema.Section, db: Session = Depends(get_db)):
    content_ = ccrud.get_content(db, content_id=section.content_id)

    if not content_:
        raise HTTPException(status_code=400, detail="no course content found matching given id")

    db_section = crud.get_section_query(db, section_id=section.id)

    if not db_section.first():
        raise HTTPException(status_code=404, detail="section not found")

    db_section.update(
        {
            "title": section.title,
            "data": section.data,
        }
    )

    db.commit()

    return crud.get_section(db, section_id=section.id)

@router.delete("/{section_id}")
async def delete_section(section_id: int, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, section_id=section_id)

    if db_section is None:
        raise HTTPException(status_code=404, detail="section not found")

    db_sec = crud.get_section_by_id(db, section_id=section_id)

    db.delete(db_sec)

    db.commit()

    return None