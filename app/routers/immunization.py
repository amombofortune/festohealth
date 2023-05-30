from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/immunization",
     tags=['Immunization']


)


""" IMMUNIZATION APIs """
# Create immunization

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_immunization(immunization: schemas.ImmunizationCreate, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    new_immunization = models.Immunization(**immunization.dict())
    db.add(new_immunization)
    db.commit()
    db.refresh(new_immunization)
    return new_immunization

# Read One immunization


@router.get("/{id}", response_model=schemas.ImmunizationResponse)
def get_immunization(id: int, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    immunization = db.query(models.Immunization).filter(
        models.Immunization.id == id).first()

    if not immunization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Immunization with id: {id} was not found")
    return immunization

# Read All immunization


@router.get("/", response_model=List[schemas.ImmunizationResponse])
def get_immunization(db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    immunization = db.query(models.Immunization).all()
    return immunization

# Update immunization


@router.put("/{id}", response_model=schemas.ImmunizationResponse)
def update_immunization(id: int, updated_immunization: schemas.ImmunizationCreate, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):

    immunization_query = db.query(models.Immunization).filter(
        models.Immunization.id == id)

    immunization = immunization_query.first()

    if immunization == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Immunization with id: {id} does not exist")

    immunization_query.update(
        updated_immunization.dict(), synchronize_session=False)
    db.commit()
    return immunization_query.first()


# Delete immunization
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_immunization(id: int, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):

    immunization = db.query(models.Immunization).filter(
        models.Immunization.id == id)

    if immunization.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Immunization with id: {id} does not exist")

    immunization.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)