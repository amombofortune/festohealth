from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter, Query
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2
from sqlalchemy.orm.exc import NoResultFound

router = APIRouter(
     prefix="/patient",
     tags=['Patient']


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


""" PATIENT APIs """
# Create patient
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_patient(
    patient: schemas.PatientCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user),
):
    existing_patient = db.query(models.Patient).filter_by(user_id=current_user.id).first()
    if existing_patient:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Patient registration form has already been submitted",
        )

    if patient.insurance == "no":
        # Set insurance fields to None when insurance is "no"
        patient.provider_name = None
        patient.policy_number = None
        patient.group_number = None
        patient.effective_date = None
        patient.expiration_date = None

    patient_obj = models.Patient(user_id=current_user.id, **patient.dict())
    db.add(patient_obj)
    db.commit()
    db.refresh(patient_obj)

    # Update registration status
    update_registration_status(current_user.id, db)

    return patient_obj




# Read single patient
@router.get("/{id}", response_model=schemas.PatientResponse)
def get_patient(id: str, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == id).first()

    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id: {id} was not found")
    return patient

# Read All patient
@router.get("/all", response_model=List[schemas.PatientResponse])
def get_patient(db: Session = Depends(get_db)):
    patient = db.query(models.Patient).all()
    return patient

# Update patient
@router.put("/{id}", response_model=schemas.PatientResponse)
def update_patient(id: str, updated_patient: schemas.PatientCreate, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):

    patient_query = db.query(models.Patient).filter(models.Patient.id == id)

    patient = patient_query.first()

    if patient == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id: {id} does not exist")
    
    if patient.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    patient_query.update(updated_patient.dict(), synchronize_session=False)
    db.commit()
    return patient_query.first()


# Delete patient
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(id: str, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):

    patient_query = db.query(models.Patient).filter(models.Patient.id == id)

    patient = patient_query.first()

    if patient == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id: {id} does not exist")
    
    if patient.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    patient_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

