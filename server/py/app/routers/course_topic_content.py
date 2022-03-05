from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import  Session, select

from app.dependencies import get_session
from app.models.models import *

#from ..dependencies import get_token_header

router = APIRouter(
    prefix="/course-topic-content",
    tags=["course-topic-content"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=CourseContentRead)
async def create_course_topic_content(*, session: Session = Depends(get_session), course_topic: CourseContentCreate):
    db_ct = CourseContent.from_orm(course_topic)
    session.add(db_ct)
    session.commit()
    session.refresh(db_ct)
    
    return db_ct

@router.get("/", response_model=List[CourseContentRead])
async def read_course_topics(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    topics = session.exec(select(CourseContent).offset(offset).limit(limit)).all()

    return topics


@router.get("/{course_topic_id}", response_model=CourseContentRead)
async def read_course_topic(*, session: Session = Depends(get_session), course_topic_id: int):
    course_topic = session.get(CourseContent, course_topic_id)
    
    if not course_topic:
        raise HTTPException(status_code=404, detail="Course Topic Content not found")

    return course_topic