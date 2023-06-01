from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/chronic_condition",
     tags=['Chronic Condition']


)


""" CHRONIC CONDITION APIs"""
# Create Chronic condition

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_chronic_condition(chronic_condition: schemas.ChronicConditionCreate, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):
    new_chronic_condition = models.ChronicCondition(user_id= current_user.id, **chronic_condition.dict())
    db.add(new_chronic_condition)
    db.commit()
    db.refresh(new_chronic_condition)
    return new_chronic_condition

# Read One Chronic condition


@router.get("/{id}", response_model=schemas.ChronicConditionResponse)
def get_chronic_condition(id: int, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):
    chronic_condition = db.query(models.ChronicCondition).filter(
        models.ChronicCondition.id == id).first()

    if not chronic_condition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Chronic condition with id: {id} was not found")
    return chronic_condition

# Read All chronic conditions
@router.get("/", response_model=List[schemas.ChronicConditionResponse])
def get_chronic_conditions(db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    chronic_condition = db.query(models.ChronicCondition)\
    .filter(models.ChronicCondition.user_id == current_user.id)\
    .filter(models.ChronicCondition.name.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return chronic_condition

# Update chronic condition
@router.put("/{id}", response_model=schemas.ChronicConditionResponse)
def update_chronic_condition(id: int, updated_chronic_condition: schemas.ChronicConditionCreate, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):

    chronic_condition_query = db.query(models.ChronicCondition).filter(
        models.ChronicCondition.id == id)

    chronic_condition = chronic_condition_query.first()

    if chronic_condition == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Chronic condition with id: {id} does not exist")
    
    if chronic_condition.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    chronic_condition_query.update(
        updated_chronic_condition.dict(), synchronize_session=False)
    db.commit()
    return chronic_condition_query.first()


# Delete chronic condition
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_chronic_condition(id: int, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):

    chronic_condition_query = db.query(models.ChronicCondition).filter(
        models.ChronicCondition.id == id)
    
    chronic_condition = chronic_condition_query.first()

    if chronic_condition == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Chronic condition with id: {id} does not exist")
    
    if chronic_condition.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    chronic_condition_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)