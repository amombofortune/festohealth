from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/medical_device",
     tags=['Medical Device']


)


""" MEDICAL DEVICES APIs """
# Create medical device
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_medical_device(medical_device: schemas.MedicalDeviceCreate, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):
    new_medical_device = models.MedicalDevice(user_id= current_user.id, **medical_device.dict())
    db.add(new_medical_device)
    db.commit()
    db.refresh(new_medical_device)
    return new_medical_device

# Read one medical device
@router.get("/{id}", response_model=schemas.MedicalDeviceResponse)
def get_medical_device(id: int, db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):
    medical_device = db.query(models.MedicalDevice).filter(
        models.MedicalDevice.id == id).first()

    if not medical_device:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical device with id: {id} was not found")
    return medical_device

# Read All medical device


@router.get("/", response_model=List[schemas.MedicalDeviceResponse])
def get_medical_device(db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    medical_device = db.query(models.MedicalDevice)\
    .filter(models.MedicalDevice.user_id == current_user.id)\
    .filter(models.MedicalDevice.name.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return medical_device

# Update medical device


@router.put("/{id}", response_model=schemas.MedicalDeviceResponse)
def update_medical_device(id: int, updated_medical_device: schemas.MedicalDeviceCreate, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):

    medical_device_query = db.query(models.MedicalDevice).filter(
        models.MedicalDevice.id == id)

    medical_device = medical_device_query.first()

    if medical_device == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical device with id: {id} does not exist")
    
    if medical_device.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medical_device_query.update(
        updated_medical_device.dict(), synchronize_session=False)
    db.commit()
    return medical_device_query.first()


# Delete medical device
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_device(id: int, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):

    medical_device_query = db.query(models.MedicalDevice).filter(
        models.MedicalDevice.id == id)
    
    medical_device = medical_device_query.first()


    if medical_device == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical device with id: {id} does not exist")
    
    if medical_device.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medical_device_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)