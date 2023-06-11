from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2

router = APIRouter(
     prefix="/doctor",
     tags=['Doctor']


)

def update_registration_status(user_id: str, db: Session):
    user = db.query(models.User).get(user_id)
    if user:
        user.registration_form_completed = True
        db.commit()
        db.refresh(user)
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )


""" DOCTOR APIs """
# Create doctor
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db),
                  current_user: int = Depends(oauth2.get_current_user)):
    
    if doctor.membership == "no":
        # Set membership field to "no" when membership is "no"
        doctor.membership = "no"
        doctor.organization_name = None
        doctor.membership_type = None
        doctor.membership_number = None
        doctor.start_date = None
        doctor.expiration_date = None
        doctor.membership_status = None

    new_doctor = models.Doctor(user_id=current_user.id, **doctor.dict())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    # Update registration status
    update_registration_status(current_user.id, db)
    
    return new_doctor

# Read One doctor
@router.get("/{id}", response_model=schemas.DoctorResponse)
def get_doctor(id: str, db: Session = Depends(get_db)):
    

    doctor = db.query(models.Doctor).filter(models.Doctor.id == id).first()

    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor with id: {id} was not found")
    return doctor

# Read All doctor
@router.get("/", response_model=List[schemas.DoctorResponse])
def get_doctor(db: Session = Depends(get_db)):
    doctor = db.query(models.Doctor).all()
    return doctor

# Update doctor
@router.put("/{id}", response_model=schemas.DoctorResponse)
def update_doctor(id: str, updated_doctor: schemas.DoctorCreate, db: Session = Depends(get_db),
                  current_user: int = Depends(oauth2.get_current_user)):

    doctor_query = db.query(models.Doctor).filter(models.Doctor.id == id)

    doctor = doctor_query.first()

    if doctor == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor with id: {id} does not exist")
    
    if doctor.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    doctor_query.update(updated_doctor.dict(), synchronize_session=False)
    db.commit()
    return doctor_query.first()


# Delete doctor
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor(id: str, db: Session = Depends(get_db),
                  current_user: int = Depends(oauth2.get_current_user)):

    doctor_query = db.query(models.Doctor).filter(models.Doctor.id == id)

    doctor = doctor_query.first()

    if doctor == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor with id: {id} does not exist")
    
    if doctor.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    doctor_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)