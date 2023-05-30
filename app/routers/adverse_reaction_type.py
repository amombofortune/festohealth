from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from . import oauth2
from typing import List

router = APIRouter(
     prefix="/adverse_reaction_type",
     tags=['Adverse Reaction Type']

)

""" ADVERSE REACTION TYPE API """
# Create Adverse Reaction Type


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_adverse_reaction_type(adverse_reaction_type: schemas.AdverseReactionTypeCreate, db: Session = Depends(get_db),
                                 current_user: int = Depends(oauth2.get_current_user)):
    new_adverse_reaction_type = models.AdverseReactionType(user_id= current_user.id,
        **adverse_reaction_type.dict())
    db.add(new_adverse_reaction_type)
    db.commit()
    db.refresh(new_adverse_reaction_type)
    return new_adverse_reaction_type

# Read One Adverse Reaction Type


@router.get("/{id}", response_model=schemas.AdverseReactionTypeResponse)
def get_one_adverse_reaction_type(id: int, db: Session = Depends(get_db),
                                  current_user: int = Depends(oauth2.get_current_user)):
    adverse_reaction_type = db.query(models.AdverseReactionType).filter(
        models.AdverseReactionType.id == id).first()

    if not adverse_reaction_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Adverse reaction type with id: {id} was not found")
    return adverse_reaction_type

# Read All Adverse Reaction Type


@router.get("/", response_model=List[schemas.AdverseReactionTypeResponse])
def get_adverse_reaction_types(db: Session = Depends(get_db),
                               current_user: int = Depends(oauth2.get_current_user)):
    adverse_reaction_types = db.query(models.AdverseReactionType).all()
    return adverse_reaction_types

# Update Adverse Reaction Type


@router.put("/{id}", response_model=schemas.AdverseReactionTypeResponse)
def update_adverse_reaction_type(id: int, updated_adverse_reaction_type: schemas.AdverseReactionTypeCreate, db: Session = Depends(get_db),
                                 current_user: int = Depends(oauth2.get_current_user)):

    adverse_reaction_type_query = db.query(models.AdverseReactionType).filter(
        models.AdverseReactionType.id == id)

    adverse_reaction = adverse_reaction_type_query.first()

    if adverse_reaction == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Adverse reaction type with id: {id} does not exist")
    
    if adverse_reaction.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    adverse_reaction_type_query.update(
        updated_adverse_reaction_type.dict(), synchronize_session=False)
    db.commit()
    return adverse_reaction_type_query.first()


# Delete Adverse Reaction Type
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_adverse_reaction_type(id: int, db: Session = Depends(get_db),
                                 current_user: int = Depends(oauth2.get_current_user)):

    adverse_reaction_type_query = db.query(models.AdverseReactionType).filter(
        models.AdverseReactionType.id == id)
    
    adverse_reaction_type = adverse_reaction_type_query.first()

    if adverse_reaction_type == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Adverse Reaction type with id: {id} does not exist")
    
    if adverse_reaction_type.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    adverse_reaction_type_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)