from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/patient_visit",
     tags=['Patient Visit']


)


""" PATIENT VISIT APIs """
# Create patient visit
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_patient_visit(patient_visit: schemas.PatientVisitCreate, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create patient visit"
        )
    
    patient_visit = models.PatientVisit(user_id= current_user.id, **patient_visit.dict())
    db.add(patient_visit)
    db.commit()
    db.refresh(patient_visit)
    return patient_visit

# Read single patient visit
@router.get("/{id}", response_model=schemas.PatientVisitResponse)
def get_patient_visit(id: int, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read patient visit"
        )
    
    patient_visit = db.query(models.PatientVisit).filter(
        models.PatientVisit.id == id).first()

    if not patient_visit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient visit with id: {id} was not found")
    return patient_visit

# Read All patient visit
@router.get("/", response_model=List[schemas.PatientVisitResponse])
def get_patient_visit(db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
    # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read patient visit"
        )
    
    patient_visit = db.query(models.PatientVisit)\
    .filter(models.PatientVisit.user_id == current_user.id)\
    .filter(models.PatientVisit.patient_id.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return patient_visit

# Update patient visit
@router.put("/{id}", response_model=schemas.PatientVisitResponse)
def update_patient_visit(id: int, updated_patient_visit: schemas.PatientVisitCreate, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals can update patient visit"
        )

    patient_visit_query = db.query(models.PatientVisit).filter(
        models.PatientVisit.id == id)

    patient_visit = patient_visit_query.first()

    if patient_visit == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient visit with id: {id} does not exist")
    
    if patient_visit.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    patient_visit_query.update(
        updated_patient_visit.dict(), synchronize_session=False)
    db.commit()
    return patient_visit_query.first()


# Delete patient visit
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_visit(id: int, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals can delete patient visit"
        )

    patient_visit_query = db.query(models.PatientVisit).filter(
        models.PatientVisit.id == id)
    
    patient_visit = patient_visit_query.first()


    if patient_visit == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient visit with id: {id} does not exist")
    
    if patient_visit.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    patient_visit_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
