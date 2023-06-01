from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/pharmacist",
     tags=['Pharmacist']


)


""" PHARMACIST """
# Create pharmacist


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_pharmacist(pharmacist: schemas.PharmacistCreate, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    pharmacist = models.Pharmacist(user_id= current_user.id, **pharmacist.dict())
    db.add(pharmacist)
    db.commit()
    db.refresh(pharmacist)
    return pharmacist

# Read single pharmacist


@router.get("/{id}", response_model=schemas.PharmacistResponse)
def get_pharmacist(id: str, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):
    pharmacist = db.query(models.Pharmacist).filter(
        models.Pharmacist.id == id).first()

    if not pharmacist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Pharmacist with id: {id} was not found")
    return pharmacist

# Read All pharmacist
@router.get("/", response_model=List[schemas.PharmacistResponse])
def get_pharmacist(db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    pharmacist = db.query(models.Pharmacist)\
    .filter(models.Pharmacist.user_id == current_user.id)\
    .filter(models.Pharmacist.licence_number.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return pharmacist

# Update pharmacist


@router.put("/{id}", response_model=schemas.PharmacistResponse)
def update_pharmacist(id: str, updated_pharmacist: schemas.PharmacistCreate, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):

    pharmacist_query = db.query(models.Pharmacist).filter(
        models.Pharmacist.id == id)

    pharmacist = pharmacist_query.first()

    if pharmacist == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Pharmacist with id: {id} does not exist")

    if pharmacist.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    pharmacist_query.update(
        updated_pharmacist.dict(), synchronize_session=False)
    db.commit()
    return pharmacist_query.first()


# Delete pharmacist
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pharmacist(id: str, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):

    pharmacist_query = db.query(models.Pharmacist).filter(
        models.Pharmacist.id == id)
    
    pharmacist = pharmacist_query.first()


    if pharmacist == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Pharmacist with id: {id} does not exist")
    
    if pharmacist.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    pharmacist_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
