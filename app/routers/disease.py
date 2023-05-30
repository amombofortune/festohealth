from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/disease",
     tags=['Disease']


)

""" DISEASES APIs """
# Create diseases

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_disease(disease: schemas.DiseaseCreate, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):
    new_disease = models.Disease(**disease.dict())
    db.add(new_disease)
    db.commit()
    db.refresh(new_disease)
    return new_disease

# Read One disease


@router.get("/{id}", response_model=schemas.DiseaseResponse)
def get_disease(id: int, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    disease = db.query(models.Disease).filter(models.Disease.id == id).first()

    if not disease:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Disease with id: {id} was not found")
    return disease

# Read All disease


@router.get("/", response_model=List[schemas.DiseaseResponse])
def get_disease(db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    disease = db.query(models.Disease).all()
    return disease

# Update disease


@router.put("/{id}", response_model=schemas.DiseaseResponse)
def update_disease(id: int, updated_disease: schemas.DiseaseCreate, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):

    disease_query = db.query(models.Disease).filter(models.Disease.id == id)

    disease = disease_query.first()

    if disease == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Disease with id: {id} does not exist")

    disease_query.update(updated_disease.dict(), synchronize_session=False)
    db.commit()
    return disease_query.first()


# Delete disease
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_disease(id: int, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):

    disease = db.query(models.Disease).filter(models.Disease.id == id)

    if disease.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Disease with id: {id} does not exist")

    disease.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)