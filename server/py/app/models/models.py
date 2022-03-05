from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

#from .team import *

class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")

class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


class Team(TeamBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    heroes: List["Hero"] = Relationship(back_populates="team")

class TeamCreate(TeamBase):
    pass

class TeamRead(TeamBase):
    id: int


class TeamUpdate(SQLModel):
    id: Optional[int] = None
    name: Optional[str] = None
    headquarters: Optional[str] = None

class HeroRead(HeroBase):
    id: int

class TeamReadWithHeroes(TeamRead):
    heroes: List[HeroRead] = []


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    team: Optional[Team] = Relationship(back_populates="heroes")

class HeroCreate(HeroBase):
    pass

class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    team_id: Optional[int] = None


class HeroReadWithTeam(HeroRead):
    team: Optional[TeamRead] = None

################################# TEACHER ########################
class TeacherBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    created_on: str = Field(default=None)

class TeacherRead(TeacherBase):
    id: int

class Teacher(TeacherBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class TeacherCreate(TeacherBase):
    pass

class TeacherUpdate(SQLModel):
    name: Optional[str] = None

# ############################## COURSE-CONTENT-BASE ###########################
class CourseTopicBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    topic: str 

class CourseTopic(CourseTopicBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: List["CourseContent"] = Relationship(back_populates="course_topic")

class CourseContentBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    created_on: str = Field(default=None)
    title: str
    content: str = Field(default=None)
    editor_teacher_id: Optional[int] = Field(default=None, foreign_key="teacher.id")
    topic_id: Optional[int] = Field(default=None, foreign_key="coursecontent.id")
    course_topic: Optional[CourseTopic] = Relationship(back_populates="content")

class CourseContentRead(CourseContentBase):
    id: int

class CourseContent(CourseContentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    teacher: Optional[Teacher] = Relationship()

class CourseContentCreate(CourseContentBase):
    pass

class CourseContentUpdate(SQLModel):
    title: Optional[str] = None
    content: Optional[str] = None
    editor_teacher_id: Optional[int] = None

############################ COURSETOPIC #####################
'''
    course topic which has a list of [CourseContent]
    e.g for Biology Course > Intro to Bio, Reproduction, Photosynthesis
'''
class CourseTopicRead(CourseTopicBase):
    id: int


class CourseTopicCreate(CourseTopicBase):
    pass

class CourseTopicUpdate(SQLModel):
    topic: Optional[str] = None

class CourseTopicWithContent(CourseTopicRead):
    content: List[CourseContentRead] = []