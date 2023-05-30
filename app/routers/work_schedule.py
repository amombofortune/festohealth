from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/work_schedule",
     tags=['Work Schedule']


)


"""WORK SCHEDULE APIs """
# Create work schedule


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_work_schedule(work_schedule: schemas.WorkScheduleCreate, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):
    work_schedule = models.WorkSchedule(user_id= current_user.id, **work_schedule.dict())
    db.add(work_schedule)
    db.commit()
    db.refresh(work_schedule)
    return work_schedule

# Read single work schedule


@router.get("/{id}", response_model=schemas.WorkScheduleResponse)
def get_work_schedule(id: int, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    work_schedule = db.query(models.WorkSchedule).filter(models.WorkSchedule.id == id).first()

    if not work_schedule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Work schedule with id: {id} was not found")
    return work_schedule

# Read All work schedules


@router.get("/", response_model=List[schemas.WorkScheduleResponse])
def get_work_schedule(db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    work_schedule = db.query(models.WorkSchedule).all()
    return work_schedule

# Update work schedule


@router.put("/{id}", response_model=schemas.WorkScheduleResponse)
def update_work_schedule(id: int, updated_work_schedule: schemas.WorkScheduleCreate, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):

    work_schedule_query = db.query(models.WorkSchedule).filter(models.WorkSchedule.id == id)

    work_schedule = work_schedule_query.first()

    if work_schedule == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Work schedule with id: {id} does not exist")
    
    if work_schedule.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    work_schedule_query.update(updated_work_schedule.dict(), synchronize_session=False)
    db.commit()
    return work_schedule_query.first()


# Delete work schedule
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_work_schedule(id: int, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):

    work_schedule_query = db.query(models.WorkSchedule).filter(models.WorkSchedule.id == id)

    work_schedule = work_schedule_query.first()


    if work_schedule == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Work schedule with id: {id} does not exist")
    
    if work_schedule.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    work_schedule_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)