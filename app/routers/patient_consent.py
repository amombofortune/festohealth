from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/patient_consent",
     tags=['Patient Consent']


)


""" PATIENT CONSENT APIs """
# Create patient consent


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_patient_consent(patient_consent: schemas.PatientConsentCreate, db: Session = Depends(get_db),
                           user_id: int = Depends(oauth2.get_current_user)):
    patient_consent = models.PatientConsent(**patient_consent.dict())
    db.add(patient_consent)
    db.commit()
    db.refresh(patient_consent)
    return patient_consent

# Read single patient consent


@router.get("/{id}", response_model=schemas.PatientConsentResponse)
def get_patient_consent(id: int, db: Session = Depends(get_db),
                        user_id: int = Depends(oauth2.get_current_user)):
    patient_consent = db.query(models.PatientConsent).filter(
        models.PatientConsent.id == id).first()

    if not patient_consent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient consent with id: {id} was not found")
    return patient_consent

# Read All patient consents


@router.get("/", response_model=List[schemas.PatientConsentResponse])
def get_patient_consent(db: Session = Depends(get_db),
                        user_id: int = Depends(oauth2.get_current_user)):
    patient_consent = db.query(models.PatientConsent).all()
    return patient_consent

# Update patient consent


@router.put("/{id}", response_model=schemas.PatientConsentResponse)
def update_patient_consent(id: int, updated_patient_consent: schemas.PatientConsentCreate, db: Session = Depends(get_db),
                           user_id: int = Depends(oauth2.get_current_user)):

    patient_consent_query = db.query(models.PatientConsent).filter(
        models.PatientConsent.id == id)

    patient_consent = patient_consent_query.first()

    if patient_consent == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient consent with id: {id} does not exist")

    patient_consent_query.update(
        updated_patient_consent.dict(), synchronize_session=False)
    db.commit()
    return patient_consent_query.first()


# Delete patient consent
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_consent(id: int, db: Session = Depends(get_db),
                           user_id: int = Depends(oauth2.get_current_user)):

    patient_consent = db.query(models.PatientConsent).filter(
        models.PatientConsent.id == id)

    if patient_consent.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient consent with id: {id} does not exist")

    patient_consent.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)