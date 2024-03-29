from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/patient_consent",
     tags=['Patient Consent']


)


""" PATIENT CONSENT APIs """
# Create patient consent
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_patient_consent(patient_consent: schemas.PatientConsentCreate, db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):
    
      # Check if the current user has the "patient" role
    if current_user.user_type != "patient":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create patient consent"
        )
    
    patient_consent = models.PatientConsent(user_id= current_user.id, **patient_consent.dict())
    db.add(patient_consent)
    db.commit()
    db.refresh(patient_consent)
    return patient_consent

# Read single patient consent
@router.get("/{id}", response_model=schemas.PatientConsentResponse)
def get_patient_consent(id: int, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    
      # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read patient consent"
        )
    
    patient_consent = db.query(models.PatientConsent).filter(
        models.PatientConsent.id == id).first()

    if not patient_consent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient consent with id: {id} was not found")
    return patient_consent

# Read All patient consents
@router.get("/", response_model=List[schemas.PatientConsentResponse])
def get_patient_consent(db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
      # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read patient consent"
        )
    
    patient_consent = db.query(models.PatientConsent)\
    .filter(models.PatientConsent.user_id == current_user.id)\
    .filter(models.PatientConsent.consent_type.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return patient_consent

# Update patient consent
@router.put("/{id}", response_model=schemas.PatientConsentResponse)
def update_patient_consent(id: int, updated_patient_consent: schemas.PatientConsentCreate, db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):
    
      # Check if the current user has the "patient" role
    if current_user.user_type != "patient":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create patient consent"
        )

    patient_consent_query = db.query(models.PatientConsent).filter(
        models.PatientConsent.id == id)

    patient_consent = patient_consent_query.first()

    if patient_consent == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient consent with id: {id} does not exist")
    
    if patient_consent.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    patient_consent_query.update(
        updated_patient_consent.dict(), synchronize_session=False)
    db.commit()
    return patient_consent_query.first()


# Delete patient consent
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_consent(id: int, db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "patient" role
    if current_user.user_type != "patient":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create patient consent"
        )

    patient_consent_query = db.query(models.PatientConsent).filter(
        models.PatientConsent.id == id)
    
    patient_consent = patient_consent_query.first()


    if patient_consent == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient consent with id: {id} does not exist")
    
    if patient_consent.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    patient_consent_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)