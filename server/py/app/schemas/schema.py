
from pydantic import BaseModel
from datetime import datetime


########################## USER #############################

class UserLogin(BaseModel):
    name: str
    password: str

class UserBase(BaseModel):
    name: str
    

class UserCreate(UserBase):
    password: str
    is_admin: bool = False
    is_teacher: bool = True
    is_student: bool = False

class User(UserBase):
    id: int
    created_on: datetime
    is_admin: bool = False
    is_teacher: bool = True
    is_student: bool = False
    
    class Config:
        orm_mode = True

############################## RESOURCE ##############
class ResourceBase(BaseModel):
    type: str
    filename: str
    filepath: str
    url: str = ''
    belong_to: str = ''
    course_background: bool = False

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int
    created_on: datetime
    
    def url(self):
        # TODO generate dynamic url from server base url
        return self.filepath + self.filename

    class Config:
        orm_mode = True

################### SECTION ####################
class SectionBase(BaseModel):
    title: str
    data: str = ""
    

class SectionCreate(SectionBase):
    pass


class Section(SectionBase):
    id: int
    content_id: int
    created_on: datetime
    updated_on: datetime
    resources: list[Resource] = []
    user_id: int | None = None
    
    class Config:
        orm_mode = True

################### CONTENT ####################
class ContentBase(BaseModel):
    topic: str
    description: str

class ContentCreate(ContentBase):
    pass


class Content(ContentBase):
    id: int
    course_id: int
    sections: list[Section] = []
    created_on: datetime
    updated_on: datetime
    
    class Config:
        orm_mode = True


################################## COURSE ################
class CourseBase(BaseModel):
    form: str | None = None
    name: str
    description: str | None = None
    synopsis: str | None = None
    color: str | None = None
    

class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    content: list[Content] = []
    resources: list[Resource] = []
    created_on: datetime
    updated_on: datetime

    class Config:
        orm_mode = True