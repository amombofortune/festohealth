from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/patient",
     tags=['Patient']


)


""" PATIENT APIs """
# Create patient


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db),
                   user_id: int = Depends(oauth2.get_current_user)):
    patient = models.Patient(**patient.dict())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

# Read single patient


@router.get("/{id}", response_model=schemas.PatientResponse)
def get_patient(id: str, db: Session = Depends(get_db),
                user_id: int = Depends(oauth2.get_current_user)):
    patient = db.query(models.Patient).filter(models.Patient.id == id).first()

    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id: {id} was not found")
    return patient

# Read All patient


@router.get("/", response_model=List[schemas.PatientResponse])
def get_patient(db: Session = Depends(get_db),
                user_id: int = Depends(oauth2.get_current_user)):
    patient = db.query(models.Patient).all()
    return patient

# Update patient


@router.put("/{id}", response_model=schemas.PatientResponse)
def update_patient(id: str, updated_patient: schemas.PatientCreate, db: Session = Depends(get_db),
                   user_id: int = Depends(oauth2.get_current_user)):

    patient_query = db.query(models.Patient).filter(models.Patient.id == id)

    patient = patient_query.first()

    if patient == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id: {id} does not exist")

    patient_query.update(updated_patient.dict(), synchronize_session=False)
    db.commit()
    return patient_query.first()


# Delete patient
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(id: str, db: Session = Depends(get_db),
                   user_id: int = Depends(oauth2.get_current_user)):

    patient = db.query(models.Patient).filter(models.Patient.id == id)

    if patient.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id: {id} does not exist")

    patient.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)