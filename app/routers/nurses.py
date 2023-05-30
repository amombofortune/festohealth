from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/nurse",
     tags=['Nurse']


)


""" NURSES APIs """
# Create nurse


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_nurse(nurse: schemas.NurseCreate, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):
    new_nurse = models.Nurse(**nurse.dict())
    db.add(new_nurse)
    db.commit()
    db.refresh(new_nurse)
    return new_nurse

# Read one nurse


@router.get("/{id}", response_model=schemas.NurseResponse)
def get_nurse(id: str, db: Session = Depends(get_db),
              current_user: int = Depends(oauth2.get_current_user)):
    nurse = db.query(models.Nurse).filter(
        models.Nurse.id == id).first()

    if not nurse:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Nurse with id: {id} was not found")
    return nurse

# Read All nurse


@router.get("/", response_model=List[schemas.NurseResponse])
def get_nurse(db: Session = Depends(get_db),
              current_user: int = Depends(oauth2.get_current_user)):
    nurse = db.query(models.Nurse).all()
    return nurse

# Update nurse


@router.put("/{id}", response_model=schemas.NurseResponse)
def update_nurse(id: str, updated_nurse: schemas.NurseCreate, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):

    nurse_query = db.query(models.Nurse).filter(
        models.Nurse.id == id)

    nurse = nurse_query.first()

    if nurse == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Nurse with id: {id} does not exist")

    nurse_query.update(updated_nurse.dict(),
                       synchronize_session=False)
    db.commit()
    return nurse_query.first()


# Delete nurse
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_nurse(id: str, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):

    nurse = db.query(models.Nurse).filter(models.Nurse.id == id)

    if nurse.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Nurse with id: {id} does not exist")

    nurse.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
