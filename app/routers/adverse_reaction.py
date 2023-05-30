from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from . import oauth2
from typing import List

router = APIRouter(
     prefix="/adverse_reaction",
     tags=['Adverse Reaction']


)


""" ADVERSE REACTIONS API """
# Create Adverse Reaction


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_adverse_reaction(adverse_reaction: schemas.AdverseReactionCreate, db: Session = Depends(get_db),
                            current_user: int = Depends(oauth2.get_current_user)):
    new_adverse_reaction = models.AdverseReaction(user_id= current_user.id, **adverse_reaction.dict())
    db.add(new_adverse_reaction)
    db.commit()
    db.refresh(new_adverse_reaction)
    return new_adverse_reaction

# Read One Adverse Reaction


@router.get("/{id}", response_model=schemas.AdverseReactionResponse)
def get_one_adverse_reaction(id: int, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):
    adverse_reaction = db.query(models.AdverseReaction).filter(
        models.AdverseReaction.id == id).first()

    if not adverse_reaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Adverse reaction with id: {id} was not found")
    return adverse_reaction

# Read All Adverse Reaction


@router.get("/", response_model=List[schemas.AdverseReactionResponse])
def get_adverse_reactions(db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):
    adverse_reactions = db.query(models.AdverseReaction).all()
    return adverse_reactions

# Update Adverse Reaction


@router.put("/{id}", response_model=schemas.AdverseReactionResponse)
def update_adverse_reaction(id: int, updated_adverse_reaction: schemas.AdverseReactionCreate, db: Session = Depends(get_db),
                            current_user: int = Depends(oauth2.get_current_user)):

    adverse_reaction_query = db.query(models.AdverseReaction).filter(
        models.AdverseReaction.id == id)

    adverse_reaction = adverse_reaction_query.first()

    if adverse_reaction == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"allergy with id: {id} does not exist")
    
    if adverse_reaction.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    adverse_reaction_query.update(
        updated_adverse_reaction.dict(), synchronize_session=False)
    db.commit()
    return adverse_reaction_query.first()


# Delete Adverse Reaction
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_adverse_reaction(id: int, db: Session = Depends(get_db),
                            current_user: int = Depends(oauth2.get_current_user)):

    adverse_reaction_query = db.query(models.AdverseReaction).filter(models.AdverseReaction.id == id)

    adverse_reaction = adverse_reaction_query.first()

    if adverse_reaction == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Adverse Reaction with id: {id} does not exist")
    
    if adverse_reaction.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    adverse_reaction_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)