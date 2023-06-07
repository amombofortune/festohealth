from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2

router = APIRouter(
     prefix="/appointment",
     tags=['Appointment']


)


""" APPOINTMENTS API """
# Create Appointment
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "doctor" or "patient" role
    if current_user.user_type not in ["doctor", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors and patients can create appointments"
        )

    
    new_appointment = models.Appointment(user_id= current_user.id, **appointment.dict())
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment

# Read One Appointment
@router.get("/{id}", response_model=schemas.AppointmentResponse)
def get_single_appointment(id: int, db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "doctor" or "patient" role
    if current_user.user_type not in ["doctor", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors and patients can read appointments"
        )
    
    appointment = db.query(models.Appointment).filter(
        models.Appointment.id == id).first()

    if not appointment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment with appointment_id: {id} was not found")
    return appointment

# Read All Appointments
@router.get("/", response_model=List[schemas.AppointmentResponse])
def get_appointment(db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    

     # Check if the current user has the "doctor" or "patient" role
    if current_user.user_type not in ["doctor", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors and patients can read appointments"
        )
    

    appointment = db.query(models.Appointment)\
    .filter(models.Appointment.user_id == current_user.id)\
    .filter(models.Appointment.status.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return appointment

# Update Appointment
@router.put("/{id}", response_model=schemas.AppointmentResponse)
def update_appointment(id: int, updated_appointment: schemas.AppointmentCreate, db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):
    

     # Check if the current user has the "doctor" or "patient" role
    if current_user.user_type not in ["doctor", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors and patients can update appointments"
        )
    
    appointment_query = db.query(models.Appointment).filter(
        models.Appointment.id == id)

    appointment = appointment_query.first()

    if appointment == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment with id: {id} does not exist")
    
    if appointment.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    appointment_query.update(updated_appointment.dict(),
                             synchronize_session=False)
    db.commit()
    return appointment_query.first()


# Delete Appointment
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment(id: int, db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" or "patient" role
    if current_user.user_type not in ["doctor", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors and patients can delete appointments"
        )
    

    appointment_query = db.query(models.Appointment).filter(
        models.Appointment.id == id)
    
    appointment = appointment_query.first()

    if appointment == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment with id: {id} does not exist")
    
    if appointment.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    appointment_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)