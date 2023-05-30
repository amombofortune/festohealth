from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/insurance_claim",
     tags=['Insurance Claim']


)


""" INSURANCE CLAIM APIs """
# Create insurance claims


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_insurance_claim(insurance_claim: schemas.InsuranceClaimCreate, db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):
    new_insurance_claim = models.InsuranceClaim(user_id= current_user.id, **insurance_claim.dict())
    db.add(new_insurance_claim)
    db.commit()
    db.refresh(new_insurance_claim)
    return new_insurance_claim

# Read one insurance claim


@router.get("/{id}", response_model=schemas.InsuranceClaimResponse)
def get_insurance_claim(id: str, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    insurance_claim = db.query(models.InsuranceClaim).filter(
        models.InsuranceClaim.id == id).first()

    if not insurance_claim:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance claim with id: {id} was not found")
    return insurance_claim

# Read All insurance claim


@router.get("/", response_model=List[schemas.InsuranceClaimResponse])
def get_insurance_claim(db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    insurance_claim = db.query(models.InsuranceClaim).all()
    return insurance_claim

# Update insurance claim


@router.put("/{id}", response_model=schemas.InsuranceClaimResponse)
def update_insurance_claim(id: str, updated_insurance_claim: schemas.InsuranceClaimCreate, db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):

    insurance_claim_query = db.query(models.InsuranceClaim).filter(
        models.InsuranceClaim.id == id)

    insurance_claim = insurance_claim_query.first()

    if insurance_claim == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance claim with id: {id} does not exist")

    if insurance_claim.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    insurance_claim_query.update(
        updated_insurance_claim.dict(), synchronize_session=False)
    db.commit()
    return insurance_claim_query.first()


# Delete insurance claim
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_insurance_claim(id: str, db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):

    insurance_claim_query = db.query(models.InsuranceClaim).filter(
        models.InsuranceClaim.id == id)
    
    insurance_claim = insurance_claim_query.first()


    if insurance_claim == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance claim with id: {id} does not exist")
    
    if insurance_claim.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    insurance_claim_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)