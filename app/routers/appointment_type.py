from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from .. import oauth2

router = APIRouter(
     prefix="/appointment_type",
     tags=['Appointment Type']


)


""" APPOINTMENT TYPE API """
# Create Appointment type


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_appointment_type(appointment_type: schemas.AppointmentTypeCreate, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):
    new_appointment_type = models.AppointmentType(user_id= current_user.id, **appointment_type.dict())
    db.add(new_appointment_type)
    db.commit()
    db.refresh(new_appointment_type)
    return new_appointment_type

# Read One Appointment type


@router.get("/{id}", response_model=schemas.AppointmentTypeResponse)
def get_single_appointment_type(id: int, db: Session = Depends(get_db),
                                current_user: int = Depends(oauth2.get_current_user)):
    appointment_type = db.query(models.AppointmentType).filter(
        models.AppointmentType.id == id).first()

    if not appointment_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment type with id: {id} was not found")
    return appointment_type

# Read All Appointment type


@router.get("/", response_model=List[schemas.AppointmentTypeResponse])
def get_appointment_type(db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):
    appointment_type = db.query(models.AppointmentType).all()
    return appointment_type

# Update Appointment type


@router.put("/{id}", response_model=schemas.AppointmentTypeResponse)
def update_appointment_type(id: int, updated_appointment_type: schemas.AppointmentTypeCreate, db: Session = Depends(get_db),
                            current_user: int = Depends(oauth2.get_current_user)):

    appointment_type_query = db.query(models.AppointmentType).filter(
        models.AppointmentType.id == id)

    appointment_type = appointment_type_query.first()

    if appointment_type == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment type with id: {id} does not exist")
    
    if appointment_type.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    appointment_type_query.update(updated_appointment_type.dict(),
                             synchronize_session=False)
    db.commit()
    return appointment_type_query.first()


# Delete Appointment type
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment_type(id: int, db: Session = Depends(get_db),
                            current_user: int = Depends(oauth2.get_current_user)):

    appointment_type_query = db.query(models.AppointmentType).filter(
        models.AppointmentType.id == id)
    
    appointment_type = appointment_type_query.first()

    if appointment_type == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Appointment type with id: {id} does not exist")
    
    if appointment_type.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    appointment_type_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)