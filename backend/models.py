from sqlalchemy import Column, Integer, String, DateTime
from database import Base, engine

class AssignmentDB(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(String, index=True)
    title = Column(String, index=True)
    due_date = Column(DateTime)
    status = Column(String, default="pending")


Base.metadata.create_all(bind=engine)
