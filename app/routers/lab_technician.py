from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/lab_technician",
     tags=['Lab Technician']


)


""" LAB TECHNICIAN APIs """
# Create lab technician
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_lab_technician(lab_technician: schemas.LabTechnicianCreate, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):
    new_lab_technician = models.LabTechnician(user_id= current_user.id, **lab_technician.dict())
    db.add(new_lab_technician)
    db.commit()
    db.refresh(new_lab_technician)
    return new_lab_technician

# Read one lab technician


@router.get("/{id}", response_model=schemas.LabTechnicianResponse)
def get_lab_technician(id: str, db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):
    lab_technician = db.query(models.LabTechnician).filter(
        models.LabTechnician.id == id).first()

    if not lab_technician:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab technician with id: {id} was not found")
    return lab_technician

# Read All lab technician


@router.get("/", response_model=List[schemas.LabTechnicianResponse])
def get_lab_technicians(db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    lab_technicians = db.query(models.LabTechnician).filter(models.LabTechnician.user_id == current_user.id).all()
    return lab_technicians

# Update lab tests


@router.put("/{id}", response_model=schemas.LabTechnicianResponse)
def update_lab_technician(id: str, updated_lab_technician: schemas.LabTechnicianCreate, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):

    lab_technician_query = db.query(models.LabTechnician).filter(
        models.LabTechnician.id == id)

    lab_technician = lab_technician_query.first()

    if lab_technician == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab technician with id: {id} does not exist")
    
    if lab_technician.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    lab_technician_query.update(
        updated_lab_technician.dict(), synchronize_session=False)
    db.commit()
    return lab_technician_query.first()


# Delete lab test
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lab_technician(id: str, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):

    lab_technician_query = db.query(models.LabTechnician).filter(
        models.LabTechnician.id == id)
    
    lab_technician = lab_technician_query.first()


    if lab_technician == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab technician with id: {id} does not exist")
    
    if lab_technician.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    lab_technician_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)