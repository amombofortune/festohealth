from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/medical_procedure",
     tags=['Medical Procedure']


)


""" MEDICAL PROCEDURES APIs """
# Create medical procedure


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_medical_procedure(medical_procedure: schemas.MedicalProcedureCreate, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create medical procedure"
        )
    
    new_medical_procedure = models.MedicalProcedure(user_id= current_user.id, **medical_procedure.dict())
    db.add(new_medical_procedure)
    db.commit()
    db.refresh(new_medical_procedure)
    return new_medical_procedure

# Read one medical procedure
@router.get("/{id}", response_model=schemas.MedicalProcedureResponse)
def get_medical_procedure(id: int, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read medical procedure"
        )
    
    medical_procedure = db.query(models.MedicalProcedure).filter(
        models.MedicalProcedure.id == id).first()

    if not medical_procedure:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical procedure with id: {id} was not found")
    return medical_procedure

# Read All medical procedures
@router.get("/", response_model=List[schemas.MedicalProcedureResponse])
def get_medical_procedure(db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
     # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read medical procedure"
        )
    
    medical_procedures = db.query(models.MedicalProcedure)\
    .filter(models.MedicalProcedure.user_id == current_user.id)\
    .filter(models.MedicalProcedure.name.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return medical_procedures

# Update medical procedure
@router.put("/{id}", response_model=schemas.MedicalProcedureResponse)
def update_medical_procedure(id: int, updated_medical_procedure: schemas.MedicalProcedureCreate, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create medical procedure"
        )

    medical_procedure_query = db.query(models.MedicalProcedure).filter(
        models.MedicalProcedure.id == id)

    medical_procedure = medical_procedure_query.first()

    if medical_procedure == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical procedure with id: {id} does not exist")
    
    if medical_procedure.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medical_procedure_query.update(
        updated_medical_procedure.dict(), synchronize_session=False)
    db.commit()
    return medical_procedure_query.first()


# Delete medical procedure
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_procedure(id: int, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create medical procedure"
        )

    medical_procedure_query = db.query(models.MedicalProcedure).filter(
        models.MedicalProcedure.id == id)
    
    medical_procedure = medical_procedure_query.first()

    if medical_procedure == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical procedure with id: {id} does not exist")
    
    if medical_procedure.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medical_procedure_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)