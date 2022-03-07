from pydantic import BaseModel


########################## USER #############################

class UserBase(BaseModel):
    name: str
    is_admin: bool
    is_teacher: bool

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True

################### SECTION ####################
class SectionBase(BaseModel):
    title: str
    data: str
    user_id: int | None = None

class SectionCreate(SectionBase):
    pass


class Section(SectionBase):
    id: int
    content_id: int
    
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
    
    class Config:
        orm_mode = True


################################## COURSE ################
class CourseBase(BaseModel):
    form: str
    name: str
    description: str | None = None
    synopsis: str | None = None

class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    content: list[Content] = []

    class Config:
        orm_mode = True