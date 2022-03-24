from enum import Enum

class ResourceTypeEnum(str, Enum):
    video = 'video'
    test = 'test'
    exercise = 'exercise'
    exam = 'exam'
    book = 'book'
    assignment = 'assignment'
    other = 'other'

class ResourceParent(str, Enum):
    section='section'
    course='course'

