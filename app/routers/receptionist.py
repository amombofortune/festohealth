from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/receptionist",
     tags=['Receptionist']


)


""" RECEPTIONIST """
# Create receptionist


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_receptionist(receptionist: schemas.ReceptionistCreate, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):
    receptionist = models.Receptionist(user_id= current_user.id, **receptionist.dict())
    db.add(receptionist)
    db.commit()
    db.refresh(receptionist)
    return receptionist

# Read single receptionist


@router.get("/{id}", response_model=schemas.ReceptionistResponse)
def get_receptionist(id: str, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    receptionist = db.query(models.Receptionist).filter(
        models.Receptionist.id == id).first()

    if not receptionist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Receptionist with id: {id} was not found")
    return receptionist

# Read All receptionists


@router.get("/", response_model=List[schemas.ReceptionistResponse])
def get_receptionist(db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    receptionist = db.query(models.Receptionist).all()
    return receptionist

# Update receptionist


@router.put("/{id}", response_model=schemas.ReceptionistResponse)
def update_receptionist(id: str, updated_receptionist: schemas.ReceptionistCreate, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):

    receptionist_query = db.query(models.Receptionist).filter(
        models.Receptionist.id == id)

    receptionist = receptionist_query.first()

    if receptionist == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Receptionist with id: {id} does not exist")
    
    if receptionist.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    receptionist_query.update(
        updated_receptionist.dict(), synchronize_session=False)
    db.commit()
    return receptionist_query.first()


# Delete receptionist
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_receptionist(id: str, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):

    receptionist_query = db.query(models.Receptionist).filter(
        models.Receptionist.id == id)
    
    receptionist = receptionist_query.first()


    if receptionist == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Receptionist with id: {id} does not exist")
    
    if receptionist.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    receptionist_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)