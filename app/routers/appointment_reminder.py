from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2

router = APIRouter(
     prefix="/appointment_reminder",
     tags=['Appointment Reminder']


)


""" APPOINTMENT REMINDERS API """
# Create Appointment Reminder


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_appointment_reminder(appointment_reminder: schemas.AppointmentReminderCreate, db: Session = Depends(get_db),
                                current_user: int = Depends(oauth2.get_current_user)):
    new_appointment_reminder = models.AppointmentReminder(user_id= current_user.id,
        **appointment_reminder.dict())
    db.add(new_appointment_reminder)
    db.commit()
    db.refresh(new_appointment_reminder)
    return new_appointment_reminder

# Read One Appointment Reminder


@router.get("/{id}", response_model=schemas.AppointmentReminderResponse)
def get_single_appointment_reminder(id: int, db: Session = Depends(get_db),
                                    current_user: int = Depends(oauth2.get_current_user)):
    appointment_reminder = db.query(models.AppointmentReminder).filter(
        models.AppointmentReminder.id == id).first()

    if not appointment_reminder:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment Reminder with id: {id} was not found")
    return appointment_reminder

# Read All Appointment Reminder


@router.get("/", response_model=List[schemas.AppointmentReminderResponse])
def get_appointment_reminders(db: Session = Depends(get_db),
                              current_user: int = Depends(oauth2.get_current_user)):
    appointment_reminder = db.query(models.AppointmentReminder).all()
    return appointment_reminder

# Update Appointment Reminder


@router.put("/{id}", response_model=schemas.AppointmentReminderResponse)
def update_appointment_reminder(id: int, updated_appointment_reminder: schemas.AppointmentReminderCreate, db: Session = Depends(get_db),
                                current_user: int = Depends(oauth2.get_current_user)):

    appointment_reminder_query = db.query(models.AppointmentReminder).filter(
        models.AppointmentReminder.id == id)

    appointment_reminder = appointment_reminder_query.first()

    if appointment_reminder == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment Reminder with reminder_id: {id} does not exist")
    
    if appointment_reminder.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    appointment_reminder_query.update(
        updated_appointment_reminder.dict(), synchronize_session=False)
    db.commit()
    return appointment_reminder_query.first()


# Delete Appointment Reminder
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment_reminder(id: int, db: Session = Depends(get_db),
                                current_user: int = Depends(oauth2.get_current_user)):

    appointment_reminder_query = db.query(models.AppointmentReminder).filter(
        models.AppointmentReminder.id == id)
    
    appointment_reminder = appointment_reminder_query.first()

    if appointment_reminder == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment Reminder with reminder_id: {id} does not exist")
    
    if appointment_reminder.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    appointment_reminder_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
