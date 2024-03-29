from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/lab_result",
     tags=['Lab Results']


)


""" LAB TEST RESULT APIs """
# Create lab test result
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_lab_result(lab_result: schemas.LabResultCreate, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "lab_technician":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only lab technician can create lab result"
        )
    
    new_lab_result = models.LabResult(user_id= current_user.id, **lab_result.dict())
    db.add(new_lab_result)
    db.commit()
    db.refresh(new_lab_result)
    return new_lab_result

# Read one lab test result
@router.get("/{id}", response_model=schemas.LabResultResponse)
def get_lab_result(id: int, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient", "lab_technician"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals, patients or lab technicians can read lab test"
        )
    
    lab_result = db.query(models.LabResult).filter(
        models.LabResult.id == id).first()

    if not lab_result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab result with id: {id} was not found")
    return lab_result

# Read All lab tests result
@router.get("/", response_model=List[schemas.LabResultResponse])
def get_lab_result(db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
     # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient", "lab_technician"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals, patients or lab technicians can read lab test"
        )
    
    lab_results = db.query(models.LabResult)\
    .filter(models.LabResult.user_id == current_user.id)\
    .filter(models.LabResult.diagnosis.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return lab_results

# Update lab tests result
@router.put("/{id}", response_model=schemas.LabResultResponse)
def update_lab_result(id: int, updated_lab_result: schemas.LabResultCreate, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "lab_technician":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only lab technician can delete lab result"
        )

    lab_result_query = db.query(models.LabResult).filter(
        models.LabResult.id == id)

    lab_result = lab_result_query.first()

    if lab_result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab result with id: {id} does not exist")
    
    if lab_result.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    lab_result_query.update(
        updated_lab_result.dict(), synchronize_session=False)
    db.commit()
    return lab_result_query.first()


# Delete lab test result
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lab_result(id: int, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "lab_technician":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only lab technician can delete lab result"
        )

    lab_result_query = db.query(models.LabResult).filter(
        models.LabResult.id == id)
    
    lab_result = lab_result_query.first()


    if lab_result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab result with id: {id} does not exist")
    
    if lab_result.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    lab_result_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)