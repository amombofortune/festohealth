from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2

router = APIRouter(
     prefix="/bed_assignment",
     tags=['Bed Assignment']


)


""" BED ASSIGNMENT APIs"""
# Create Bed assignment
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_bed_assignment(bed_assignment: schemas.BedAssignmentCreate, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):
    new_bed_assignment = models.BedAssignment(user_id= current_user.id, **bed_assignment.dict())
    db.add(new_bed_assignment)
    db.commit()
    db.refresh(new_bed_assignment)
    return new_bed_assignment

# Read One Bed Assignment


@router.get("/{id}", response_model=schemas.BedAssignmentResponse)
def get_bed_assignment(id: int, db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):
    bed_assignment = db.query(models.BedAssignment).filter(
        models.BedAssignment.id == id).first()

    if not bed_assignment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed with id: {id} was not found")
    return bed_assignment

# Read All Bed Assignment


@router.get("/", response_model=List[schemas.BedAssignmentResponse])
def get_bed_assignment(db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):
    bed_assignment = db.query(models.BedAssignment).all()
    return bed_assignment

# Update Bed Assignment


@router.put("/{id}", response_model=schemas.BedAssignmentResponse)
def update_bed_assignment(id: int, updated_bed_assignment: schemas.BedAssignmentCreate, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):

    bed_assignment_query = db.query(models.BedAssignment).filter(
        models.BedAssignment.id == id)

    bed_assignment = bed_assignment_query.first()

    if bed_assignment == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed assignment with id: {id} does not exist")
    
    if bed_assignment.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    bed_assignment_query.update(
        updated_bed_assignment.dict(), synchronize_session=False)
    db.commit()
    return bed_assignment_query.first()


# Delete Bed Assignment
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bed(id: int, db: Session = Depends(get_db),
               current_user: int = Depends(oauth2.get_current_user)):

    bed_assignment_query = db.query(models.BedAssignment).filter(
        models.BedAssignment.id == id)
    
    bed_assignment = bed_assignment_query.first()

    if bed_assignment == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bed assignment with id: {id} does not exist")
    
    if bed_assignment.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    bed_assignment_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)