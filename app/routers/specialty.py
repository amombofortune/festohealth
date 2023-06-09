from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from .. import oauth2


router = APIRouter(
     prefix="/specialty",
     tags=['Specialty']


)


""" SPECIALTY APIs"""
# Create specialty
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_specialty(specialty: schemas.SpecialtyCreate, db: Session = Depends(get_db)):
    specialty = models.Specialty( **specialty.dict())
    db.add(specialty)
    db.commit()
    db.refresh(specialty)
    return specialty

# Read single specialty
@router.get("/{id}", response_model=schemas.SpecialtyResponse)
def get_specialty(id: int, db: Session = Depends(get_db)):
    specialty = db.query(models.Specialty).filter(models.Specialty.id == id).first()

    if not specialty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Specialty with id: {id} was not found")
    return specialty

# Read All specialty
@router.get("/", response_model=List[schemas.SpecialtyResponse])
def get_specialty(db: Session = Depends(get_db)):
    specialty = db.query(models.Specialty).all()
    return specialty

# Update specialty
@router.put("/{id}", response_model=schemas.SpecialtyResponse)
def update_specialty(id: int, updated_specialty: schemas.SpecialtyCreate, db: Session = Depends(get_db)):

    specialty_query = db.query(models.Specialty).filter(models.Specialty.id == id)

    specialty = specialty_query.first()

    if specialty == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Specialty with id: {id} does not exist")


    specialty_query.update(
        updated_specialty.dict(), synchronize_session=False)
    db.commit()
    return specialty_query.first()


# Delete specialty
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_specialty(id: int, db: Session = Depends(get_db)):

    specialty_query = db.query(models.Specialty).filter(models.Specialty.id == id)

    specialty = specialty_query.first()


    if specialty == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Specialty with id: {id} does not exist")


    specialty_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
