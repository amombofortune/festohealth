from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/medication",
     tags=['Medication']


)



""" MEDICATION APIs """
# Create medication


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_medication(medication: schemas.MedicationCreate, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    new_medication = models.Medication(**medication.dict())
    db.add(new_medication)
    db.commit()
    db.refresh(new_medication)
    return new_medication

# Read one medication


@router.get("/{id}", response_model=schemas.MedicationResponse)
def get_medication(id: int, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):
    medication = db.query(models.Medication).filter(
        models.Medication.id == id).first()

    if not medication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medication with id: {id} was not found")
    return medication

# Read All medication


@router.get("/", response_model=List[schemas.MedicationResponse])
def get_medication(db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):
    medication = db.query(models.Medication).all()
    return medication

# Update medication


@router.put("/{id}", response_model=schemas.MedicationResponse)
def update_medication(id: int, updated_medication: schemas.MedicationCreate, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):

    medication_query = db.query(models.Medication).filter(
        models.Medication.id == id)

    medication = medication_query.first()

    if medication == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medication with id: {id} does not exist")

    medication_query.update(updated_medication.dict(),
                            synchronize_session=False)
    db.commit()
    return medication_query.first()


# Delete medication
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medication(id: int, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):

    medication = db.query(models.Medication).filter(models.Medication.id == id)

    if medication.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medication with id: {id} does not exist")

    medication.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
