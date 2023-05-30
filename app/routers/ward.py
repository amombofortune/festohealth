from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/ward",
     tags=['Ward']


)



"""WARD APIs """
# Create ward


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_ward(ward: schemas.WardCreate, db: Session = Depends(get_db),
                user_id: int = Depends(oauth2.get_current_user)):
    ward = models.Ward(**ward.dict())
    db.add(ward)
    db.commit()
    db.refresh(ward)
    return ward

# Read single ward


@router.get("/{id}", response_model=schemas.WardResponse)
def get_ward(id: int, db: Session = Depends(get_db),
             user_id: int = Depends(oauth2.get_current_user)):
    ward = db.query(models.Ward).filter(models.Ward.id == id).first()

    if not ward:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Ward with id: {id} was not found")
    return ward

# Read All ward


@router.get("/", response_model=List[schemas.WardResponse])
def get_ward(db: Session = Depends(get_db),
             user_id: int = Depends(oauth2.get_current_user)):
    ward = db.query(models.Ward).all()
    return ward

# Update ward


@router.put("/{id}", response_model=schemas.WardResponse)
def update_ward(id: int, updated_ward: schemas.WardCreate, db: Session = Depends(get_db),
                user_id: int = Depends(oauth2.get_current_user)):

    ward_query = db.query(models.Ward).filter(models.Ward.id == id)

    ward = ward_query.first()

    if ward == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Ward with id: {id} does not exist")

    ward_query.update(updated_ward.dict(), synchronize_session=False)
    db.commit()
    return ward_query.first()


# Delete ward
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ward(id: int, db: Session = Depends(get_db),
                user_id: int = Depends(oauth2.get_current_user)):

    ward = db.query(models.Ward).filter(models.Ward.id == id)

    if ward.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Ward with id: {id} does not exist")

    ward.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)