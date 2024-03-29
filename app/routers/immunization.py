from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/immunization",
     tags=['Immunization']


)


""" IMMUNIZATION APIs """
# Create immunization
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_immunization(immunization: schemas.ImmunizationCreate, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create immunization"
        )
    
    new_immunization = models.Immunization(user_id= current_user.id, **immunization.dict())
    db.add(new_immunization)
    db.commit()
    db.refresh(new_immunization)
    return new_immunization

# Read One immunization
@router.get("/{id}", response_model=schemas.ImmunizationResponse)
def get_immunization(id: int, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):

     # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read immunization"
        )
    
    immunization = db.query(models.Immunization).filter(
        models.Immunization.id == id).first()

    if not immunization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Immunization with id: {id} was not found")
    return immunization

# Read All immunization
@router.get("/", response_model=List[schemas.ImmunizationResponse])
def get_immunization(db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
     # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read immunization"
        )

    immunization = db.query(models.Immunization)\
    .filter(models.Immunization.user_id == current_user.id)\
    .filter(models.Immunization.vaccine_name.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return immunization

# Update immunization
@router.put("/{id}", response_model=schemas.ImmunizationResponse)
def update_immunization(id: int, updated_immunization: schemas.ImmunizationCreate, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can update immunization"
        )

    immunization_query = db.query(models.Immunization).filter(
        models.Immunization.id == id)

    immunization = immunization_query.first()

    if immunization == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Immunization with id: {id} does not exist")
    
    if immunization.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    immunization_query.update(
        updated_immunization.dict(), synchronize_session=False)
    db.commit()
    return immunization_query.first()


# Delete immunization
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_immunization(id: int, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can delete immunization"
        )

    immunization_query = db.query(models.Immunization).filter(
        models.Immunization.id == id)
    
    immunization = immunization_query.first()


    if immunization == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Immunization with id: {id} does not exist")
    
    if immunization.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    immunization_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)