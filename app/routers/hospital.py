from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/hospital",
     tags=['Hospital']


)

def update_registration_status(user_id: str, db: Session):
    user = db.query(models.User).get(user_id)
    if user:
        user.registration_form_completed = True
        db.commit()
        db.refresh(user)
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

""" HOSPITAL APIs """
# Create hospital
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_hospital(hospital: schemas.HospitalCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    
    existing_hospital = db.query(models.Hospital).filter_by(user_id=current_user.id).first()
    if existing_hospital:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Hospital registration form has already been submitted",
        )
    
    if hospital.accreditation == "no":
        # Set accreditation fields to None when accreditation is "no"
        hospital.accreditation_authority = None
        hospital.accreditation_date = None
        hospital.accreditation_level = None
        hospital.expiry_date = None

    provider_obj = models.Hospital(user_id=current_user.id, **hospital.dict())
    db.add(provider_obj)
    db.commit()
    db.refresh(provider_obj)

    # Update registration status
    update_registration_status(current_user.id, db)

    return provider_obj

# Read One hospital


@router.get("/{id}", response_model=schemas.HospitalResponse)
def get_hospital(id: str, db: Session = Depends(get_db)):
    hospital = db.query(models.Hospital).filter(
        models.Hospital.id == id).first()

    if not hospital:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Hospital with id: {id} was not found")
    return hospital

# Read All hospitals


@router.get("/", response_model=List[schemas.HospitalResponse])
def get_hospital(db: Session = Depends(get_db)):
    hospital = db.query(models.Hospital).all()
    return hospital

# Update hospital


@router.put("/{id}", response_model=schemas.HospitalResponse)
def update_hospital(id: str, updated_hospital: schemas.HospitalCreate, db: Session = Depends(get_db)):

    hospital_query = db.query(models.Hospital).filter(models.Hospital.id == id)

    hospital = hospital_query.first()

    if hospital == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Hospital with id: {id} does not exist")
    

    hospital_query.update(updated_hospital.dict(), synchronize_session=False)
    db.commit()
    return hospital_query.first()


# Delete hospital
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hospital(id: str, db: Session = Depends(get_db)):

    hospital_query = db.query(models.Hospital).filter(models.Hospital.id == id)

    hospital = hospital_query.first()


    if hospital == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Hospital with id: {id} does not exist")

    hospital_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)