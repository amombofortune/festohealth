from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from .. import oauth2


router = APIRouter(
     prefix="/doctor_membership",
     tags=['Doctor Membership Bodies']
)

""" DOCTOR MEMBERSHIPS APIs"""
# Create Country
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_doctor_membership(doctor_membership: schemas.DoctorMembershipCreate, db: Session = Depends(get_db)):
    new_doctor_membership = models.DoctorMembership(**doctor_membership.dict())
    db.add(new_doctor_membership)
    db.commit()
    db.refresh(new_doctor_membership)
    return new_doctor_membership

# Read One membership
@router.get("/{id}", response_model=schemas.DoctorMembershipResponse)
def get_doctor_membership(id: int, db: Session = Depends(get_db)):
    doctor_membership = db.query(models.DoctorMembership).filter(models.DoctorMembership.id == id).first()

    if not doctor_membership:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor Membership with id: {id} was not found")
    return doctor_membership

# Read All Memberships
@router.get("/", response_model=List[schemas.DoctorMembershipResponse])
def get_doctor_membership(db: Session = Depends(get_db)):
    doctor_membership = db.query(models.DoctorMembership).all()
    return doctor_membership

# Update Membership
@router.put("/{id}", response_model=schemas.DoctorMembershipResponse)
def update_doctor_membership(id: int, updated_doctor_membership: schemas.DoctorMembershipCreate, db: Session = Depends(get_db)):

    doctor_membership_query = db.query(models.DoctorMembership).filter(models.DoctorMembership.id == id)

    doctor_membership = doctor_membership_query.first()

    if doctor_membership == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor Membership with id: {id} does not exist")


    doctor_membership_query.update(updated_doctor_membership.dict(), synchronize_session=False)
    db.commit()
    return doctor_membership_query.first()


# Delete membership
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor_membership(id: int, db: Session = Depends(get_db)):

    doctor_membership_query = db.query(models.DoctorMembership).filter(models.DoctorMembership.id == id)

    doctor_membership = doctor_membership_query.first()

    if doctor_membership == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor membership with id: {id} does not exist")
    

    doctor_membership_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
