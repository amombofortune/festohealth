from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/genetic_condition",
     tags=['Genetic Condition']


)


""" GENETIC CONDITION APIs """
# Create genetic condition


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_genetic_condition(genetic_condition: schemas.GeneticConditionCreate, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):
    new_genetic_condition = models.GeneticCondition(user_id= current_user.id, **genetic_condition.dict())
    db.add(new_genetic_condition)
    db.commit()
    db.refresh(new_genetic_condition)
    return new_genetic_condition

# Read One genetic condition


@router.get("/{id}", response_model=schemas.GeneticConditionResponse)
def get_genetic_condition(id: int, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):
    genetic_condition = db.query(models.GeneticCondition).filter(
        models.GeneticCondition.id == id).first()

    if not genetic_condition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Genetic condition with id: {id} was not found")
    return genetic_condition

# Read All genetic conditions


@router.get("/", response_model=List[schemas.GeneticConditionResponse])
def get_genetic_condition(db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    genetic_condition = db.query(models.GeneticCondition)\
    .filter(models.GeneticCondition.user_id == current_user.id)\
    .filter(models.GeneticCondition.name.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return genetic_condition

# Update genetic condition


@router.put("/{id}", response_model=schemas.GeneticConditionResponse)
def update_genetic_condition(id: int, updated_genetic_condition: schemas.GeneticConditionCreate, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):

    genetic_condition_query = db.query(models.GeneticCondition).filter(
        models.GeneticCondition.id == id)

    genetic_condition = genetic_condition_query.first()

    if genetic_condition == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Genetic condition with id: {id} does not exist")
    
    if genetic_condition.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    genetic_condition_query.update(
        updated_genetic_condition.dict(), synchronize_session=False)
    db.commit()
    return genetic_condition_query.first()


# Delete genetic condition
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_genetic_condition(id: int, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):

    genetic_condition_query = db.query(models.GeneticCondition).filter(
        models.GeneticCondition.id == id)
    
    genetic_condition = genetic_condition_query.first()

    if genetic_condition == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Genetic condition with id: {id} does not exist")
    
    if genetic_condition.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    genetic_condition_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)