from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from .. import oauth2
from typing import List, Optional

router = APIRouter(
     prefix="/adverse_reaction",
     tags=['Adverse Reaction']


)


""" ADVERSE REACTIONS API """
# Create Adverse Reaction


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_adverse_reaction(adverse_reaction: schemas.AdverseReactionCreate, db: Session = Depends(get_db),
                            current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create adverse reaction"
        )
    
    new_adverse_reaction = models.AdverseReaction(user_id= current_user.id, **adverse_reaction.dict())
    db.add(new_adverse_reaction)
    db.commit()
    db.refresh(new_adverse_reaction)
    return new_adverse_reaction

# Read One Adverse Reaction
@router.get("/{id}", response_model=schemas.AdverseReactionResponse)
def get_one_adverse_reaction(id: int, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" or "patient" role
    if current_user.user_type not in ["doctor", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors and patients can read adverse reaction"
        )
    
    adverse_reaction = db.query(models.AdverseReaction).filter(
        models.AdverseReaction.id == id).first()

    if not adverse_reaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Adverse reaction with id: {id} was not found")
    return adverse_reaction

# Read All Adverse Reaction
@router.get("/", response_model=List[schemas.AdverseReactionResponse])
def get_adverse_reactions(db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
     # Check if the current user has the "doctor" or "patient" role
    if current_user.user_type not in ["doctor", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors and patients can read adverse reaction"
        )
    
    adverse_reactions = db.query(models.AdverseReaction)\
        .filter(models.AdverseReaction.user_id == current_user.id)\
        .filter(models.AdverseReaction.treatment.ilike(f'%{search}%'))\
        .limit(limit)\
        .offset(skip)\
        .all() #return for that user only
    return adverse_reactions

# Update Adverse Reaction
@router.put("/{id}", response_model=schemas.AdverseReactionResponse)
def update_adverse_reaction(id: int, updated_adverse_reaction: schemas.AdverseReactionCreate, db: Session = Depends(get_db),
                            current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can update adverse reaction"
        )
    

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
    
    # Check if the current user has the "doctor" role
    if current_user.user_type != "patient":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only patient can delete adverse reaction"
        )

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