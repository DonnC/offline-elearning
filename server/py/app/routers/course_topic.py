from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import  Session, select

from app.dependencies import get_session
from app.models.models import *

#from ..dependencies import get_token_header

router = APIRouter(
    prefix="/course-topic",
    tags=["course-topic"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=CourseTopicRead)
async def create_course_topic(*, session: Session = Depends(get_session), course_topic: CourseTopicCreate):
    db_ct = CourseTopic.from_orm(course_topic)
    session.add(db_ct)
    session.commit()
    session.refresh(db_ct)
    
    return db_ct

@router.get("/", response_model=List[CourseTopicRead])
async def read_course_topics(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    topics = session.exec(select(CourseTopic).offset(offset).limit(limit)).all()

    return topics


@router.get("/{course_topic_id}", response_model=CourseTopicWithContent)
async def read_course_topic(*, session: Session = Depends(get_session), course_topic_id: int):
    course_topic = session.get(CourseTopic, course_topic_id)
    
    if not course_topic:
        raise HTTPException(status_code=404, detail="Course Topic not found")

    return course_topic

@router.patch("/{course_topic_id}", response_model=CourseTopic)
async def update_course_topic(
    *, session: Session = Depends(get_session), course_topic_id: int, course_topic: CourseTopicUpdate
):
    db_course_topic = session.get(CourseTopic, course_topic_id)
    if not db_course_topic:
        raise HTTPException(status_code=404, detail="course topic not found")

    course_topic_data = course_topic.dict(exclude_unset=True)

    for key, value in course_topic_data.items():
        setattr(db_course_topic, key, value)

    session.add(db_course_topic)
    session.commit()
    session.refresh(db_course_topic)

    return db_course_topic


@router.delete("/{course_topic_id}")
async def delete_course_topic(*, session: Session = Depends(get_session), course_topic_id: int):
    course_topic = session.get(CourseTopic, course_topic_id)

    if not course_topic:
        raise HTTPException(status_code=404, detail="course topic not found")

    session.delete(course_topic)
    session.commit()
    
    return {
        "ok": True
    }


