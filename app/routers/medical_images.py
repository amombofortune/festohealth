from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/medical_image",
     tags=['Medical Image']


)


""" MEDICAL IMAGES APIs """
# Create medical images
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_medical_image(medical_image: schemas.MedicalImageCreate, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can create medical image"
        )
    
    new_medical_image = models.MedicalImage(user_id= current_user.id, **medical_image.dict())
    db.add(new_medical_image)
    db.commit()
    db.refresh(new_medical_image)
    return new_medical_image

# Read one medical image
@router.get("/{id}", response_model=schemas.MedicalImageResponse)
def get_medical_image(id: int, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read medical image"
        )
    
    medical_image = db.query(models.MedicalImage).filter(
        models.MedicalImage.id == id).first()

    if not medical_image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical image with id: {id} was not found")
    return medical_image

# Read All medical images
@router.get("/", response_model=List[schemas.MedicalImageResponse])
def get_medical_images(db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
      # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read medical image"
        )
    
    medical_images = db.query(models.MedicalImage)\
    .filter(models.MedicalImage.user_id == current_user.id)\
    .filter(models.MedicalImage.image_type.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return medical_images

# Update medical images
@router.put("/{id}", response_model=schemas.MedicalImageResponse)
def update_medical_image(id: int, updated_medical_image: schemas.MedicalImageCreate, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can update diagnosis"
        )

    medical_image_query = db.query(models.MedicalImage).filter(
        models.MedicalImage.id == id)

    medical_image = medical_image_query.first()

    if medical_image == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical image with id: {id} does not exist")
    
    if medical_image.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medical_image_query.update(
        updated_medical_image.dict(), synchronize_session=False)
    db.commit()
    return medical_image_query.first()


# Delete medical image
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_image(id: int, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):
    
     # Check if the current user has the "doctor" role
    if current_user.user_type != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can delete diagnosis"
        )

    medical_image_query = db.query(models.MedicalImage).filter(
        models.MedicalImage.id == id)
    
    medical_image = medical_image_query.first()


    if medical_image == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical image with id: {id} does not exist")
    
    if medical_image.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medical_image_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)