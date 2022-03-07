from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref

from app.database import Base

# system user
# e.g Teacher, Admin
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    # can be name, username or phonenumber
    name = Column(String, index=True, unique=True)
    #created_on = Column(DateTime, server_default=datetime.utcnow)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    # for anonymous signin
    is_student = Column(Boolean, default=False) 
    is_teacher = Column(Boolean, default=True)

# main course e.g
# form: form3
# name: Biology
# synopsis: In this course, you will learn about Biology and how it is important in our day to day lives for a healthy living
# description: full description about <course-name>
# content: [ <content> ]
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    # class | form e.g form4, form6, grade3
    form = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    # created_on = Column(DateTime, server_default=datetime.utcnow)
    # updated_on = Column(DateTime, server_default=datetime.utcnow, onupdate=datetime.utcnow)
    # full course description
    description = Column(String, default=None)
    # short course description
    synopsis = Column(String, default=None) 

    content = relationship("Content", back_populates="course")


# course content e.g 
# topic: Introduction
# description: Who is this for? What are we learning?
class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    # content topic | title
    topic = Column(String, index=True, unique=True)
    # short description about this content
    description = Column(String)
    # created_on = Column(DateTime, server_default=datetime.utcnow)
    # updated_on = Column(DateTime, server_default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationship with Course
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="content")

    # for course-sections
    sections = relationship("Section", back_populates="content")

# course content section e.g
# title: Plant Reproduction
# data: < data info >
class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)
    data = Column(String)

    # created_on = Column(DateTime, server_default=datetime.utcnow)
    # updated_on = Column(DateTime, server_default=datetime.utcnow, onupdate=datetime.utcnow)

    content_id = Column(Integer, ForeignKey("contents.id"))
    content = relationship("Content", back_populates="sections")

    # map editor (Teacher | Admin) to this section which has been edited
    user_id = Column(Integer, ForeignKey('users.id'))
    editor = relationship("User", backref = backref("sections", uselist=False))
