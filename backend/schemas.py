from pydantic import BaseModel
from datetime import datetime

class AssignmentBase(BaseModel):
    course_id: str
    title: str
    due_date: datetime

class AssignmentCreate(AssignmentBase):
    pass

class Assignment(AssignmentBase):
    id: int
    status: str

    class Config:
        orm_mode = True
