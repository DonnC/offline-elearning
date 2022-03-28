# learning grades enum
from enum import Enum

class GradeEnum(str, Enum):
    form1 = 'form1'
    form2 = 'form2'
    form3 = 'form3'
    form4 = 'form4'
    form5 = 'form5'
    form6 = 'form6'
    other = 'other'