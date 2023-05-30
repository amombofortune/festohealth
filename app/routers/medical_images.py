from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/medical_image",
     tags=['Medical Image']


)


""" MEDICAL IMAGES APIs """
# Create medical images


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_medical_image(medical_image: schemas.MedicalImageCreate, db: Session = Depends(get_db),
                         user_id: int = Depends(oauth2.get_current_user)):
    new_medical_image = models.MedicalImage(**medical_image.dict())
    db.add(new_medical_image)
    db.commit()
    db.refresh(new_medical_image)
    return new_medical_image

# Read one medical image


@router.get("/{id}", response_model=schemas.MedicalImageResponse)
def get_medical_image(id: int, db: Session = Depends(get_db),
                      user_id: int = Depends(oauth2.get_current_user)):
    medical_image = db.query(models.MedicalImage).filter(
        models.MedicalImage.id == id).first()

    if not medical_image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical image with id: {id} was not found")
    return medical_image

# Read All medical images


@router.get("/", response_model=List[schemas.MedicalImageResponse])
def get_medical_images(db: Session = Depends(get_db),
                       user_id: int = Depends(oauth2.get_current_user)):
    medical_images = db.query(models.MedicalImage).all()
    return medical_images

# Update medical images


@router.put("/{id}", response_model=schemas.MedicalImageResponse)
def update_medical_image(id: int, updated_medical_image: schemas.MedicalImageCreate, db: Session = Depends(get_db),
                         user_id: int = Depends(oauth2.get_current_user)):

    medical_image_query = db.query(models.MedicalImage).filter(
        models.MedicalImage.id == id)

    medical_image = medical_image_query.first()

    if medical_image == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical image with id: {id} does not exist")

    medical_image_query.update(
        updated_medical_image.dict(), synchronize_session=False)
    db.commit()
    return medical_image_query.first()


# Delete medical image
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_image(id: int, db: Session = Depends(get_db),
                         user_id: int = Depends(oauth2.get_current_user)):

    medical_image = db.query(models.MedicalImage).filter(
        models.MedicalImage.id == id)

    if medical_image.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical image with id: {id} does not exist")

    medical_image.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)