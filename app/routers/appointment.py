from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2

router = APIRouter(
     prefix="/appointment",
     tags=['Appointment']


)



""" APPOINTMENTS API """
# Create Appointment


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db),
                       user_id: int = Depends(oauth2.get_current_user)):
    new_appointment = models.Appointment(**appointment.dict())
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment

# Read One Appointment


@router.get("/{id}", response_model=schemas.AppointmentResponse)
def get_single_appointment(id: int, db: Session = Depends(get_db),
                           user_id: int = Depends(oauth2.get_current_user)):
    appointment = db.query(models.Appointment).filter(
        models.Appointment.id == id).first()

    if not appointment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment with appointment_id: {id} was not found")
    return appointment

# Read All Appointments


@router.get("/", response_model=List[schemas.AppointmentResponse])
def get_appointment(db: Session = Depends(get_db),
                    user_id: int = Depends(oauth2.get_current_user)):
    appointment = db.query(models.Appointment).all()
    return appointment

# Update Appointment


@router.put("/{id}", response_model=schemas.AppointmentResponse)
def update_appointment(id: int, updated_appointment: schemas.AppointmentCreate, db: Session = Depends(get_db),
                       user_id: int = Depends(oauth2.get_current_user)):

    appointment_query = db.query(models.Appointment).filter(
        models.Appointment.id == id)

    appointment_reminder = appointment_query.first()

    if appointment_reminder == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment with id: {id} does not exist")

    appointment_query.update(updated_appointment.dict(),
                             synchronize_session=False)
    db.commit()
    return appointment_query.first()


# Delete Appointment
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment(id: int, db: Session = Depends(get_db),
                       user_id: int = Depends(oauth2.get_current_user)):

    appointment = db.query(models.Appointment).filter(
        models.Appointment.id == id)

    if appointment.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment with id: {id} does not exist")

    appointment.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)