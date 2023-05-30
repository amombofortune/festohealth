from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/patient_feedback",
     tags=['Patient Feedback']


)



""" PATIENT FEEDBACK APIs """
# Create patient feedback


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_patient_feedback(patient_feedback: schemas.PatientFeedbackCreate, db: Session = Depends(get_db),
                             user_id: int = Depends(oauth2.get_current_user)):
    patient_feedback = models.PatientFeedback(**patient_feedback.dict())
    db.add(patient_feedback)
    db.commit()
    db.refresh(patient_feedback)
    return patient_feedback

# Read single patient feedback


@router.get("/{id}", response_model=schemas.PatientFeedbackResponse)
def get_patient_feedback(id: int, db: Session = Depends(get_db),
                         user_id: int = Depends(oauth2.get_current_user)):
    patient_feedback = db.query(models.PatientFeedback).filter(
        models.PatientFeedback.id == id).first()

    if not patient_feedback:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient feedback with id: {id} was not found")
    return patient_feedback

# Read All patient feedback


@router.get("/", response_model=List[schemas.PatientFeedbackResponse])
def get_patient_feedback(db: Session = Depends(get_db),
                         user_id: int = Depends(oauth2.get_current_user)):
    patient_feedback = db.query(models.PatientFeedback).all()
    return patient_feedback

# Update patient feedback


@router.put("/{id}", response_model=schemas.PatientFeedbackResponse)
def update_patient_feedback(id: int, updated_patient_feedback: schemas.PatientFeedbackCreate, db: Session = Depends(get_db),
                            user_id: int = Depends(oauth2.get_current_user)):

    patient_feedback_query = db.query(models.PatientFeedback).filter(
        models.PatientFeedback.id == id)

    patient_feedback = patient_feedback_query.first()

    if patient_feedback == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient feedback with id: {id} does not exist")

    patient_feedback_query.update(
        updated_patient_feedback.dict(), synchronize_session=False)
    db.commit()
    return patient_feedback_query.first()


# Delete patient feedback
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_feedback(id: int, db: Session = Depends(get_db),
                            user_id: int = Depends(oauth2.get_current_user)):

    patient_feedback = db.query(models.PatientFeedback).filter(
        models.PatientFeedback.id == id)

    if patient_feedback.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient feedback with id: {id} does not exist")

    patient_feedback.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
