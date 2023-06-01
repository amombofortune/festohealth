from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2

router = APIRouter(
     prefix="/billing",
     tags=['Billing']


)


""" BILLING APIs"""
# Create Billing


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_billing(billing: schemas.BillingCreate, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):
    new_billing = models.Billing(user_id= current_user.id, **billing.dict())
    db.add(new_billing)
    db.commit()
    db.refresh(new_billing)
    return new_billing

# Read One Billing


@router.get("/{id}", response_model=schemas.BillingResponse)
def get_billing(id: int, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    billing = db.query(models.Billing).filter(models.Billing.id == id).first()

    if not billing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Billing with id: {id} was not found")
    return billing

# Read All Billings


@router.get("/", response_model=List[schemas.BillingResponse])
def get_billing(db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    billing = db.query(models.Billing)\
    .filter(models.Billing.user_id == current_user.id)\
    .filter(models.Billing.payment_method.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return billing

# Update Billing


@router.put("/{id}", response_model=schemas.BillingResponse)
def update_billing(id: int, updated_billing: schemas.BillingCreate, db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):

    billing_query = db.query(models.Billing).filter(models.Billing.id == id)

    billing = billing_query.first()

    if billing == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Billing with id: {id} does not exist")
    
    if billing.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    billing_query.update(updated_billing.dict(), synchronize_session=False)
    db.commit()
    return billing_query.first()


# Delete Billing
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bill(id: int, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):

    billing_query = db.query(models.Billing).filter(models.Billing.id == id)

    billing = billing_query.first()


    if billing == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Billing with id: {id} does not exist")
    
    if billing.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    billing_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)