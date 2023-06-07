from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/diagnosis",
     tags=['Diagnosis']


)

""" DIAGNOSIS APIs """  # API ERROR
# Create diagnosis
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_diagnosis(diagnosis: schemas.DiagnosisCreate, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create diagnosis"
        )
    
    new_diagnosis = models.Diagnosis(user_id= current_user.id, **diagnosis.dict())
    db.add(new_diagnosis)
    db.commit()
    db.refresh(new_diagnosis)
    return new_diagnosis

# Read One diagnosis
@router.get("/{id}", response_model=schemas.DiagnosisResponse)
def get_diagnosis(id: int, db: Session = Depends(get_db),
                  current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read diagnosis"
        )
    
    diagnosis = db.query(models.Diagnosis).filter(
        models.Diagnosis.id == id).first()

    if not diagnosis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Diagnosis with id: {id} was not found")
    return diagnosis

# Read All diagnosis
@router.get("/", response_model=List[schemas.DiagnosisResponse])
def get_diagnosis(db: Session = Depends(get_db),
                  current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
     # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read diagnosis"
        )
    
    diagnosis = db.query(models.Diagnosis)\
    .filter(models.Diagnosis.user_id == current_user.id)\
    .filter(models.Diagnosis.disease.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return diagnosis

# Update diagnosis
@router.put("/{id}", response_model=schemas.DiagnosisResponse)
def update_diagnosis(id: int, updated_diagnosis: schemas.DiagnosisCreate, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    

    # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can update diagnosis"
        )

    diagnosis_query = db.query(models.Diagnosis).filter(
        models.Diagnosis.id == id)

    diagnosis = diagnosis_query.first()

    if diagnosis == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Diagnosis with id: {id} does not exist")
    
    if diagnosis.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    diagnosis_query.update(updated_diagnosis.dict(), synchronize_session=False)
    db.commit()
    return diagnosis_query.first()


# Delete diagnosis
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_diagnosis(id: int, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):

    diagnosis_query = db.query(models.Diagnosis).filter(models.Diagnosis.id == id)

    diagnosis = diagnosis_query.first()


    if diagnosis == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Diagnosis with id: {id} does not exist")
    
    if diagnosis.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    diagnosis_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)