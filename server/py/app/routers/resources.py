from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile
from sqlmodel import  Session

from os import path
from app.constants.constants import FETCH_LIMIT

from app.dependencies import get_db
from app.models import models
from app.models.resource_types_enum import ResourceParent, ResourceTypeEnum

from app.schemas import schema
from app.crud import section_crud as scrud, content_crud as ccrud, resource_crud as crud, course_crud as c_crud
from media_file_uploader import delete_file, save_upload_file

#from ..dependencies import get_token_header

router = APIRouter(
    prefix="/resources",
    tags=["resources"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/{resource_id}", response_model=schema.Resource)
async def read_resource(resource_id: int, db: Session = Depends(get_db)):
    db_res = crud.get_resource(db, resource_id=resource_id)

    if db_res is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    return db_res

@router.get("/", response_model=list[schema.Resource])
async def read_resources(skip: int = 0, limit: int = FETCH_LIMIT, db: Session = Depends(get_db)):
    res = crud.get_resources(db, skip=skip, limit=limit)
    return res

@router.get("/type/", response_model=list[schema.Resource])
async def get_resource_by_type(type: ResourceTypeEnum, db: Session = Depends(get_db)):
    res = crud.get_resource_by_type(db, type)
    return res

@router.get("/parent/", response_model=list[schema.Resource])
async def get_resource_by_parent(parent: ResourceParent, db: Session = Depends(get_db)):
    res = crud.get_resource_by_parent(db, parent)
    return res


@router.get("/section/{section_id}", response_model=list[schema.Resource])
async def get_section_resources(section_id: int,  type: Optional[ResourceTypeEnum] = None, db: Session = Depends(get_db)):
    section = scrud.get_section(db, section_id=section_id)

    if not section:
        raise HTTPException(status_code=400, detail="no course content section found matching given id")

    try:
        return crud.get_section_resources(db, section_id, type)

    except Exception as err:
        raise HTTPException(status_code=400, detail=f"failed to get section resources: {err}")


@router.get("/course/{course_id}", response_model=list[schema.Resource])
async def get_course_resources(course_id: int,  type: Optional[ResourceTypeEnum] = None, db: Session = Depends(get_db)):
    course = c_crud.get_course(db, course_id=course_id)

    if not course:
        raise HTTPException(status_code=400, detail="no course found matching given id")

    try:
        return crud.get_course_resources(db, course_id, type)

    except Exception as err:
        raise HTTPException(status_code=400, detail=f"failed to get course resources: {err}")

@router.post("/section/", response_model=schema.Resource)
async def create_section_resource(section_id: int, type: ResourceTypeEnum, file: UploadFile,  request: Request, db: Session = Depends(get_db)):
    section = scrud.get_section(db, section_id=section_id)

    if not section:
        raise HTTPException(status_code=400, detail="no course content section found matching given id")

    # get linked content
    sec_content = ccrud.get_content(db, content_id=section.content_id)

    sec_course = c_crud.get_course(db, course_id=sec_content.course_id)

    course_name = sec_course.name
    course_form_grade = sec_course.form
    content_topic = sec_content.topic
    section_title = section.title

    resource_type = type.value

    res_section_path = path.join(course_form_grade, course_name, content_topic, section_title, resource_type)

    try:
        saved_file = await save_upload_file(
            upload_file=file, 
            request=request, 
            resource_path=res_section_path
        )

        # save resource
        res  = schema.ResourceCreate(
            type=type.value,
            filename=saved_file['filename'],
            filepath=saved_file['filepath'],
            url=saved_file['url'],
            belong_to='section'
        )

        return crud.create_section_resource(db=db, section_id=section_id, resource=res)

    except Exception as err:
        raise HTTPException(status_code=400, detail=f"failed to save section resource: {err}")


@router.post("/course/", response_model=schema.Resource)
async def create_course_resource(course_id: int, type: ResourceTypeEnum, file: UploadFile,  request: Request, db: Session = Depends(get_db)):
    course = c_crud.get_course(db, course_id=course_id)

    if not course:
        raise HTTPException(status_code=400, detail="no course found matching given id")

    course_name = course.name
    course_form_grade = course.form

    resource_type = type.value

    res_section_path = path.join(course_form_grade, course_name, resource_type)

    try:
        saved_file = await save_upload_file(
            upload_file=file, 
            request=request, 
            resource_path=res_section_path
        )

        # save resource
        res  = schema.ResourceCreate(
            type=type.value,
            filename=saved_file['filename'],
            filepath=saved_file['filepath'],
            url=saved_file['url'],
            belong_to='course'
        )

        return crud.create_course_resource(db=db, course_id=course_id, resource=res)

    except Exception as err:
        raise HTTPException(status_code=400, detail=f"failed to save course resource: {err}")

@router.delete("/{resource_id}")
async def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    db_res = crud.get_resource(db, resource_id=resource_id)

    if db_res is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    res = crud.get_resource_by_id(db, resource_id=resource_id)

    db.delete(res)

    is_deleted = await delete_file(resource_path=res.filepath) 

    db.commit()

    if not is_deleted:
        raise HTTPException(status_code=404, detail="Failed to delete resource")

    return {
        "status": "OK!",
        "detail": "Resource deleted successfully"
    }