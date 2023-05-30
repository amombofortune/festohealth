from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2

router = APIRouter(
     prefix="/allergy",
     tags=['Allergy']


)

""" ALLERGY API """
# Create Allergy


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_allergy(allergy: schemas.AllergyCreate, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):
    new_allergy = models.Allergy(user_id= current_user.id, **allergy.dict())
    db.add(new_allergy)
    db.commit()
    db.refresh(new_allergy)
    return new_allergy

# Read One Allergy


@router.get("/{id}", response_model=schemas.AllergyResponse)
def get_one_allergy(id: int, db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):
    allergy = db.query(models.Allergy).filter(models.Allergy.id == id).first()

    if not allergy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Allergy with id: {id} was not found")
    return allergy

# Read All Allergies


@router.get("/", response_model=List[schemas.AllergyResponse])
def get_allergy(db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    allergy = db.query(models.Allergy).filter(models.Allergy.user_id == current_user.id).all()
    return allergy

# Update Allergy


@router.put("/{id}", response_model=schemas.AllergyResponse)
def update_allergy(id: int, updated_allergy: schemas.AllergyCreate, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):

    allergy_query = db.query(models.Allergy).filter(models.Allergy.id == id)

    allergy = allergy_query.first()

    if allergy == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Allergy with id: {id} does not exist")
    
    if allergy.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    allergy_query.update(updated_allergy.dict(), synchronize_session=False)
    db.commit()
    return allergy_query.first()


# Delete Allergy
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_allergy(id: int, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):

    allergy_query = db.query(models.Allergy).filter(models.Allergy.id == id)

    allergy = allergy_query.first()

    if allergy == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Allergy with id: {id} does not exist")
    
    if allergy.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    allergy_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)