from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import database, models, schemas

app = FastAPI()

# Allow local frontend dev server to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/assignments", response_model=List[schemas.Assignment])
def get_all_assignments(db: Session = Depends(get_db)):
    return db.query(models.AssignmentDB).all()

@app.post("/api/assignments", response_model=schemas.Assignment)
def create_assignment(assignment: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    db_item = models.AssignmentDB(
        course_id=assignment.course_id,
        title=assignment.title,
        due_date=assignment.due_date,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/api/assignments/{assignment_id}", response_model=schemas.Assignment)
def update_assignment_status(assignment_id: int, db: Session = Depends(get_db)):
    item = db.query(models.AssignmentDB).filter(models.AssignmentDB.id == assignment_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Assignment not found")
    item.status = "completed"
    db.commit()
    db.refresh(item)
    return item
