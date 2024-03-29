from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/medication",
     tags=['Medication']


)



""" MEDICATION APIs """
# Create medication
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_medication(medication: schemas.MedicationCreate, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
      # Check if the current user has the "doctor" role
    if current_user.user_type not in ["doctor", "hospital"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors or hospitals can read medication"
        )
    
    new_medication = models.Medication(user_id= current_user.id, **medication.dict())
    db.add(new_medication)
    db.commit()
    db.refresh(new_medication)
    return new_medication

# Read one medication
@router.get("/{id}", response_model=schemas.MedicationResponse)
def get_medication(id: int, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):
    
      # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read medication"
        )
    
    medication = db.query(models.Medication).filter(
        models.Medication.id == id).first()

    if not medication:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medication with id: {id} was not found")
    return medication

# Read All medication
@router.get("/", response_model=List[schemas.MedicationResponse])
def get_medication(db: Session = Depends(get_db)):
    
        medication = db.query(models.Medication).all()
        return medication

# Update medication
@router.put("/{id}", response_model=schemas.MedicationResponse)
def update_medication(id: int, updated_medication: schemas.MedicationCreate, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
      # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can update medication"
        )

    medication_query = db.query(models.Medication).filter(
        models.Medication.id == id)

    medication = medication_query.first()

    if medication == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medication with id: {id} does not exist")
    
    if medication.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medication_query.update(updated_medication.dict(),
                            synchronize_session=False)
    db.commit()
    return medication_query.first()


# Delete medication
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medication(id: int, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
      # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can delete medication"
        )

    medication_query = db.query(models.Medication).filter(models.Medication.id == id)

    medication = medication_query.first()


    if medication == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medication with id: {id} does not exist")
    
    if medication.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medication_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
