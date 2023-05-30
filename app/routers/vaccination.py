from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/vaccination",
     tags=['Vaccination']


)


""" VACCINATION APIs """
# Create vaccination


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_vaccination(vaccination: schemas.VaccinationCreate, db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):
    vaccination = models.Vaccination(user_id= current_user.id, **vaccination.dict())
    db.add(vaccination)
    db.commit()
    db.refresh(vaccination)
    return vaccination

# Read single vaccination


@router.get("/{id}", response_model=schemas.VaccinationResponse)
def get_vaccination(id: int, db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):
    vaccination = db.query(models.Vaccination).filter(
        models.Vaccination.id == id).first()

    if not vaccination:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vaccination with id: {id} was not found")
    return vaccination

# Read All vaccination


@router.get("/", response_model=List[schemas.VaccinationResponse])
def get_vaccination(db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):
    vaccination = db.query(models.Vaccination).all()
    return vaccination

# Update vaccination


@router.put("/{id}", response_model=schemas.VaccinationResponse)
def update_vaccination(id: int, updated_vaccination: schemas.VaccinationCreate, db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):

    vaccination_query = db.query(models.Vaccination).filter(
        models.Vaccination.id == id)

    vaccination = vaccination_query.first()

    if vaccination == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vaccination with id: {id} does not exist")

    if vaccination.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    vaccination_query.update(updated_vaccination.dict(),
                             synchronize_session=False)
    db.commit()
    return vaccination_query.first()


# Delete vaccination
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vaccination(id: int, db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):

    vaccination_query = db.query(models.Vaccination).filter(
        models.Vaccination.id == id)
    
    vaccination = vaccination_query.first()

    if vaccination == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vaccination with id: {id} does not exist")
    
    if vaccination.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    vaccination_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)