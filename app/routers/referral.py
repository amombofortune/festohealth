from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/referral",
     tags=['Referral']


)


""" REFERRALS """
# Create referrals


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_referral(referral: schemas.ReferralCreate, db: Session = Depends(get_db),
                    user_id: int = Depends(oauth2.get_current_user)):
    referral = models.Referral(**referral.dict())
    db.add(referral)
    db.commit()
    db.refresh(referral)
    return referral

# Read single referral


@router.get("/{id}", response_model=schemas.ReferralResponse)
def get_referral(id: int, db: Session = Depends(get_db),
                 user_id: int = Depends(oauth2.get_current_user)):
    referral = db.query(models.Referral).filter(
        models.Referral.id == id).first()

    if not referral:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Referral with id: {id} was not found")
    return referral

# Read All referrals


@router.get("/", response_model=List[schemas.ReferralResponse])
def get_referrals(db: Session = Depends(get_db),
                  user_id: int = Depends(oauth2.get_current_user)):
    referrals = db.query(models.Referral).all()
    return referrals

# Update referrals


@router.put("/{id}", response_model=schemas.ReferralResponse)
def update_referral(id: int, updated_referral: schemas.ReferralCreate, db: Session = Depends(get_db),
                    user_id: int = Depends(oauth2.get_current_user)):

    referral_query = db.query(models.Referral).filter(models.Referral.id == id)

    referral = referral_query.first()

    if referral == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Referral with id: {id} does not exist")

    referral_query.update(updated_referral.dict(), synchronize_session=False)
    db.commit()
    return referral_query.first()


# Delete referral
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_referral(id: int, db: Session = Depends(get_db),
                    user_id: int = Depends(oauth2.get_current_user)):

    referral = db.query(models.Referral).filter(models.Referral.id == id)

    if referral.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Referral with id: {id} does not exist")

    referral.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
