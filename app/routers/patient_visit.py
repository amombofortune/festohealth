from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/patient_visit",
     tags=['Patient Visit']


)


""" PATIENT VISIT APIs """
# Create patient visit


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_patient_visit(patient_visit: schemas.PatientVisitCreate, db: Session = Depends(get_db),
                         user_id: int = Depends(oauth2.get_current_user)):
    patient_visit = models.PatientVisit(**patient_visit.dict())
    db.add(patient_visit)
    db.commit()
    db.refresh(patient_visit)
    return patient_visit

# Read single patient visit


@router.get("/{id}", response_model=schemas.PatientVisitResponse)
def get_patient_visit(id: int, db: Session = Depends(get_db),
                      user_id: int = Depends(oauth2.get_current_user)):
    patient_visit = db.query(models.PatientVisit).filter(
        models.PatientVisit.id == id).first()

    if not patient_visit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient visit with id: {id} was not found")
    return patient_visit

# Read All patient visit


@router.get("/", response_model=List[schemas.PatientVisitResponse])
def get_patient_visit(db: Session = Depends(get_db),
                      user_id: int = Depends(oauth2.get_current_user)):
    patient_visit = db.query(models.PatientVisit).all()
    return patient_visit

# Update patient visit


@router.put("/{id}", response_model=schemas.PatientVisitResponse)
def update_patient_visit(id: int, updated_patient_visit: schemas.PatientVisitCreate, db: Session = Depends(get_db),
                         user_id: int = Depends(oauth2.get_current_user)):

    patient_visit_query = db.query(models.PatientVisit).filter(
        models.PatientVisit.id == id)

    patient_visit = patient_visit_query.first()

    if patient_visit == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient visit with id: {id} does not exist")

    patient_visit_query.update(
        updated_patient_visit.dict(), synchronize_session=False)
    db.commit()
    return patient_visit_query.first()


# Delete patient visit
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_visit(id: int, db: Session = Depends(get_db),
                         user_id: int = Depends(oauth2.get_current_user)):

    patient_visit = db.query(models.PatientVisit).filter(
        models.PatientVisit.id == id)

    if patient_visit.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient visit with id: {id} does not exist")

    patient_visit.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
