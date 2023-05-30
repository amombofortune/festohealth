from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/it_staff",
     tags=['IT Staff']


)


""" IT STAFF APIs """
# Create IT Staff


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_it_staff(it_staff: schemas.ItstaffCreate, db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):
    new_it_staff = models.Itstaff(user_id= current_user.id, 
        **it_staff.dict())
    db.add(new_it_staff)
    db.commit()
    db.refresh(new_it_staff)
    return new_it_staff

# Read one IT Staff


@router.get("/{id}", response_model=schemas.ItstaffResponse)
def get_it_staff(id: str, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):
    it_staff = db.query(models.Itstaff).filter(
        models.Itstaff.id == id).first()

    if not it_staff:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"IT Staff with id: {id} was not found")
    return it_staff

# Read All IT Staff


@router.get("/", response_model=List[schemas.ItstaffResponse])
def get_it_staff(db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):
    it_staff = db.query(models.Itstaff).filter(models.Itstaff.user_id == current_user.id).all()
    return it_staff

# Update IT Staff


@router.put("/{id}", response_model=schemas.ItstaffResponse)
def update_it_staff(id: str, updated_it_staff: schemas.ItstaffCreate, db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):

    it_staff_query = db.query(models.Itstaff).filter(
        models.Itstaff.id == id)

    it_staff = it_staff_query.first()

    if it_staff == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"IT Staff with id: {id} does not exist")
    
    if it_staff.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    it_staff_query.update(
        updated_it_staff.dict(), synchronize_session=False)
    db.commit()
    return it_staff_query.first()


# Delete IT Staff
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_it_staff(id: str, db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):

    it_staff_query = db.query(models.Itstaff).filter(
        models.Itstaff.id == id)
    
    it_staff = it_staff_query.first()


    if it_staff == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"IT Staff with id: {id} does not exist")
    
    if it_staff.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    it_staff_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
