from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/patient_feedback",
     tags=['Patient Feedback']


)



""" PATIENT FEEDBACK APIs """
# Create patient feedback
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_patient_feedback(patient_feedback: schemas.PatientFeedbackCreate, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "patient" role
    if current_user.user_type != "patient":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only patient can create patient feedback"
        )
    
    patient_feedback = models.PatientFeedback(user_id= current_user.id, **patient_feedback.dict())
    db.add(patient_feedback)
    db.commit()
    db.refresh(patient_feedback)
    return patient_feedback

# Read single patient feedback
@router.get("/{id}", response_model=schemas.PatientFeedbackResponse)
def get_patient_feedback(id: int, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read patient feedback"
        )
    
    patient_feedback = db.query(models.PatientFeedback).filter(
        models.PatientFeedback.id == id).first()

    if not patient_feedback:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient feedback with id: {id} was not found")
    return patient_feedback

# Read All patient feedback
@router.get("/", response_model=List[schemas.PatientFeedbackResponse])
def get_patient_feedback(db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
    # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read patient feedback"
        )
    
    patient_feedback = db.query(models.PatientFeedback)\
    .filter(models.PatientFeedback.user_id == current_user.id)\
    .filter(models.PatientFeedback.patient_id.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return patient_feedback

# Update patient feedback
@router.put("/{id}", response_model=schemas.PatientFeedbackResponse)
def update_patient_feedback(id: int, updated_patient_feedback: schemas.PatientFeedbackCreate, db: Session = Depends(get_db),
                            current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "patient" role
    if current_user.user_type != "patient":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only patient can update patient feedback"
        )

    patient_feedback_query = db.query(models.PatientFeedback).filter(
        models.PatientFeedback.id == id)

    patient_feedback = patient_feedback_query.first()

    if patient_feedback == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient feedback with id: {id} does not exist")
    
    if patient_feedback.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    patient_feedback_query.update(
        updated_patient_feedback.dict(), synchronize_session=False)
    db.commit()
    return patient_feedback_query.first()


# Delete patient feedback
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_feedback(id: int, db: Session = Depends(get_db),
                            current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "patient" role
    if current_user.user_type != "patient":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only patient can delete patient feedback"
        )

    patient_feedback_query = db.query(models.PatientFeedback).filter(
        models.PatientFeedback.id == id)
    
    patient_feedback = patient_feedback_query.first()


    if patient_feedback == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient feedback with id: {id} does not exist")
    
    if patient_feedback.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    patient_feedback_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
