from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/vital_sign",
     tags=['Vital Sign']


)



""" VITAL SIGN APIs """
# Create vital sign


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_vital_sign(vital_sign: schemas.VitalSignCreate, db: Session = Depends(get_db),
                      user_id: int = Depends(oauth2.get_current_user)):
    vital_sign = models.VitalSign(**vital_sign.dict())
    db.add(vital_sign)
    db.commit()
    db.refresh(vital_sign)
    return vital_sign

# Read single vital sign


@router.get("/{id}", response_model=schemas.VitalSignResponse)
def get_vital_sign(id: int, db: Session = Depends(get_db),
                   user_id: int = Depends(oauth2.get_current_user)):
    vital_sign = db.query(models.VitalSign).filter(
        models.VitalSign.id == id).first()

    if not vital_sign:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vital sign with id: {id} was not found")
    return vital_sign

# Read All vaccination


@router.get("/", response_model=List[schemas.VitalSignResponse])
def get_vital_sign(db: Session = Depends(get_db),
                   user_id: int = Depends(oauth2.get_current_user)):
    vital_sign = db.query(models.VitalSign).all()
    return vital_sign

# Update vaccination


@router.put("/{id}", response_model=schemas.VitalSignResponse)
def update_vital_sign(id: int, updated_vital_sign: schemas.VitalSignCreate, db: Session = Depends(get_db),
                      user_id: int = Depends(oauth2.get_current_user)):

    vital_sign_query = db.query(models.VitalSign).filter(
        models.VitalSign.id == id)

    vital_sign = vital_sign_query.first()

    if vital_sign == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vital sign with id: {id} does not exist")

    vital_sign_query.update(updated_vital_sign.dict(),
                            synchronize_session=False)
    db.commit()
    return vital_sign_query.first()


# Delete vaccination
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vital_sign(id: int, db: Session = Depends(get_db),
                      user_id: int = Depends(oauth2.get_current_user)):

    vital_sign = db.query(models.VitalSign).filter(models.VitalSign.id == id)

    if vital_sign.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vital sign with id: {id} does not exist")

    vital_sign.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
