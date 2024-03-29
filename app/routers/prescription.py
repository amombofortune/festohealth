from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/prescription",
     tags=['Prescription']


)


""" PRESCRIPTION """
# Create prescription
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_prescription(prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create prescription"
        )
    
    prescription = models.Prescription(user_id= current_user.id, **prescription.dict())
    db.add(prescription)
    db.commit()
    db.refresh(prescription)
    return prescription

# Read single prescription
@router.get("/{id}", response_model=schemas.PrescriptionResponse)
def get_prescription(id: int, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read prescription"
        )
    
    prescription = db.query(models.Prescription).filter(
        models.Prescription.id == id).first()

    if not prescription:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Prescription with id: {id} was not found")
    return prescription

# Read All prescription
@router.get("/", response_model=List[schemas.PrescriptionResponse])
def get_prescription(db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
    # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read prescription"
        )
    
    prescriptions = db.query(models.Prescription)\
    .filter(models.Prescription.user_id == current_user.id)\
    .filter(models.Prescription.medication.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return prescriptions

# Update prescription
@router.put("/{id}", response_model=schemas.PrescriptionResponse)
def update_prescription(id: int, updated_prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can update prescription"
        )

    prescription_query = db.query(models.Prescription).filter(
        models.Prescription.id == id)

    prescription = prescription_query.first()

    if prescription == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Prescription with id: {id} does not exist")
    
    if prescription.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    prescription_query.update(
        updated_prescription.dict(), synchronize_session=False)
    db.commit()
    return prescription_query.first()


# Delete prescription
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prescription(id: int, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can delete prescription"
        )

    prescription_query = db.query(models.Prescription).filter(
        models.Prescription.id == id)
    
    prescription = prescription_query.first()


    if prescription == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Prescription with id: {id} does not exist")
    
    if prescription.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    prescription_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)