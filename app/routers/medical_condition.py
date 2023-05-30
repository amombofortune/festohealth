from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/medical_condition",
     tags=['Medical Condition']


)


""" MEDICAL CONDITION APIs """
# Create medical condition
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_medical_condition(medical_condition: schemas.MedicalConditionCreate, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):
    new_medical_condition = models.MedicalCondition(user_id= current_user.id, **medical_condition.dict())
    db.add(new_medical_condition)
    db.commit()
    db.refresh(new_medical_condition)
    return new_medical_condition

# Read one medical condition


@router.get("/{id}", response_model=schemas.MedicalConditionResponse)
def get_medical_condition(id: int, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):
    medical_condition = db.query(models.MedicalCondition).filter(
        models.MedicalCondition.id == id).first()

    if not medical_condition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical condition with id: {id} was not found")
    return medical_condition

# Read All medical condition


@router.get("/", response_model=List[schemas.MedicalConditionResponse])
def get_medical_condition(db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):
    medical_condition = db.query(models.MedicalCondition).all()
    return medical_condition

# Update medical condition


@router.put("/{id}", response_model=schemas.MedicalConditionResponse)
def update_medical_condition(id: int, updated_medical_condition: schemas.MedicalConditionCreate, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):

    medical_condition_query = db.query(models.MedicalCondition).filter(
        models.MedicalCondition.id == id)

    medical_condition = medical_condition_query.first()

    if medical_condition == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical condition with id: {id} does not exist")
    
    if medical_condition.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medical_condition_query.update(
        updated_medical_condition.dict(), synchronize_session=False)
    db.commit()
    return medical_condition_query.first()


# Delete medical condition
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_condition(id: int, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):

    medical_condition_query = db.query(models.MedicalCondition).filter(
        models.MedicalCondition.id == id)
    
    medical_condition = medical_condition_query.first()


    if medical_condition == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical condition with id: {id} does not exist")
    
    if medical_condition.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medical_condition_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)