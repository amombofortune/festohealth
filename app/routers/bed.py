from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2

router = APIRouter(
     prefix="/bed",
     tags=['Bed']


)


""" BED APIs"""
# Create Bed


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_bed(bed: schemas.BedCreate, db: Session = Depends(get_db),
               current_user: int = Depends(oauth2.get_current_user)):
    new_bed = models.Bed(user_id= current_user.id, **bed.dict())
    db.add(new_bed)
    db.commit()
    db.refresh(new_bed)
    return new_bed

# Read One Bed


@router.get("/{id}", response_model=schemas.BedResponse)
def get_bed(id: int, db: Session = Depends(get_db),
            current_user: int = Depends(oauth2.get_current_user)):
    bed = db.query(models.Bed).filter(models.Bed.id == id).first()

    if not bed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed with id: {id} was not found")
    return bed

# Read All Bed


@router.get("/", response_model=List[schemas.BedResponse])
def get_beds(db: Session = Depends(get_db),
             current_user: int = Depends(oauth2.get_current_user)):
    bed = db.query(models.Bed).all()
    return bed

# Update Bed


@router.put("/{id}", response_model=schemas.BedResponse)
def update_bed(id: int, updated_bed: schemas.BedCreate, db: Session = Depends(get_db),
               current_user: int = Depends(oauth2.get_current_user)):

    bed_query = db.query(models.Bed).filter(models.Bed.id == id)

    bed = bed_query.first()

    if bed == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed with bed_reminder: {id} does not exist")
    
    if bed.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    bed_query.update(updated_bed.dict(), synchronize_session=False)
    db.commit()
    return bed_query.first()


# Delete Bed
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bed(id: int, db: Session = Depends(get_db),
               current_user: int = Depends(oauth2.get_current_user)):

    bed_query = db.query(models.Bed).filter(models.Bed.id == id)

    bed = bed_query.first()


    if bed == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed with id: {id} does not exist")
    
    if bed.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    bed_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)