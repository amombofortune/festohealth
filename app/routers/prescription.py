from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/prescription",
     tags=['Prescription']


)


""" PRESCRIPTION """
# Create prescription


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_prescription(prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db),
                        user_id: int = Depends(oauth2.get_current_user)):
    prescription = models.Prescription(**prescription.dict())
    db.add(prescription)
    db.commit()
    db.refresh(prescription)
    return prescription

# Read single prescription


@router.get("/{id}", response_model=schemas.PrescriptionResponse)
def get_prescription(id: int, db: Session = Depends(get_db),
                     user_id: int = Depends(oauth2.get_current_user)):
    prescription = db.query(models.Prescription).filter(
        models.Prescription.id == id).first()

    if not prescription:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Prescription with id: {id} was not found")
    return prescription

# Read All prescription


@router.get("/", response_model=List[schemas.PrescriptionResponse])
def get_prescription(db: Session = Depends(get_db),
                     user_id: int = Depends(oauth2.get_current_user)):
    prescriptions = db.query(models.Prescription).all()
    return prescriptions

# Update prescription


@router.put("/{id}", response_model=schemas.PrescriptionResponse)
def update_prescription(id: int, updated_prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db),
                        user_id: int = Depends(oauth2.get_current_user)):

    prescription_query = db.query(models.Prescription).filter(
        models.Prescription.id == id)

    prescription = prescription_query.first()

    if prescription == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Prescription with id: {id} does not exist")

    prescription_query.update(
        updated_prescription.dict(), synchronize_session=False)
    db.commit()
    return prescription_query.first()


# Delete prescription
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prescription(id: int, db: Session = Depends(get_db),
                        user_id: int = Depends(oauth2.get_current_user)):

    prescription = db.query(models.Prescription).filter(
        models.Prescription.id == id)

    if prescription.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Prescription with id: {id} does not exist")

    prescription.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)