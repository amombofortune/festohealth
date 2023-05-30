from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/time_slot",
     tags=['Time Slot']


)


""" TIME SLOTS APIs"""
# Create time slot 
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_time_slot(time_slot: schemas.TimeSlotCreate, db: Session = Depends(get_db),
                     user_id: int = Depends(oauth2.get_current_user)):
    time_slot = models.TimeSlot(**time_slot.dict())
    db.add(time_slot)
    db.commit()
    db.refresh(time_slot)
    return time_slot

# Read single time slot


@router.get("/{id}", response_model=schemas.TimeSlotResponse)
def get_time_slot(id: int, db: Session = Depends(get_db),
                  user_id: int = Depends(oauth2.get_current_user)):
    time_slot = db.query(models.TimeSlot).filter(models.TimeSlot.id == id).first()

    if not time_slot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Time slot with id: {id} was not found")
    return time_slot

# Read All time slots


@router.get("/", response_model=List[schemas.TimeSlotResponse])
def get_time_slot(db: Session = Depends(get_db),
                  user_id: int = Depends(oauth2.get_current_user)):
    time_slot = db.query(models.TimeSlot).all()
    return time_slot

# Update time slot


@router.put("/{id}", response_model=schemas.TimeSlotResponse)
def update_time_slot(id: str, updated_time_slot: schemas.TimeSlotCreate, db: Session = Depends(get_db),
                     user_id: int = Depends(oauth2.get_current_user)):

    time_slot_query = db.query(models.TimeSlot).filter(models.TimeSlot.id == id)

    time_slot = time_slot_query.first()

    if time_slot == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Time slot with id: {id} does not exist")

    time_slot_query.update(
        updated_time_slot.dict(), synchronize_session=False)
    db.commit()
    return time_slot_query.first()


# Delete time slot
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_time_slot(id: int, db: Session = Depends(get_db),
                     user_id: int = Depends(oauth2.get_current_user)):

    time_slot = db.query(models.TimeSlot).filter(models.TimeSlot.id == id)

    if time_slot.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Time slot with id: {id} does not exist")

    time_slot.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
