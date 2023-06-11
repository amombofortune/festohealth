from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/insurance_provider",
     tags=['Insurance Provider']


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

""" INSURANCE PROVIDER APIs """
# Create insurance providers

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_insurance_provider(insurance_provider: schemas.InsuranceProviderCreate, db: Session = Depends(get_db),current_user: models.User = Depends(oauth2.get_current_user)):

    existing_provider = db.query(models.InsuranceProvider).filter_by(user_id=current_user.id).first()
    if existing_provider:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insurance provider registration form has already been submitted",
        )

    if insurance_provider.certification == "no":
        # Set insurance fields to None when insurance is "no"
        insurance_provider.certification_type = None
        insurance_provider.certification_number = None
        insurance_provider.issuing_authority = None
        insurance_provider.issue_date = None
        insurance_provider.expiration_date = None

    provider_obj = models.InsuranceProvider(user_id=current_user.id, **insurance_provider.dict())
    db.add(provider_obj)
    db.commit()
    db.refresh(provider_obj)

    # Update registration status
    update_registration_status(current_user.id, db)

    return provider_obj


# Read one insurance provider
@router.get("/{id}", response_model=schemas.InsuranceProviderResponse)
def get_insurance_provider(id: str, db: Session = Depends(get_db)):
    insurance_provider = db.query(models.InsuranceProvider).filter(
        models.InsuranceProvider.id == id).first()

    if not insurance_provider:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance provider with id: {id} was not found")
    return insurance_provider

# Read All insurance providers
@router.get("/", response_model=List[schemas.InsuranceProviderResponse])
def get_insurance_provider(db: Session = Depends(get_db)):
    insurance_provider = db.query(models.InsuranceProvider).all()
    return insurance_provider

# Update insurance provider


@router.put("/{id}", response_model=schemas.InsuranceProviderResponse)
def update_insurance_provider(id: str, updated_insurance_company: schemas.InsuranceProviderCreate, db: Session = Depends(get_db)):

    insurance_provider_query = db.query(models.InsuranceProvider).filter(
        models.InsuranceProvider.id == id)

    insurance_provider = insurance_provider_query.first()

    if insurance_provider == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance company with id: {id} does not exist")

    insurance_provider_query.update(
        updated_insurance_company.dict(), synchronize_session=False)
    db.commit()
    return insurance_provider_query.first()


# Delete insurance provider
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_insurance_provider(id: str, db: Session = Depends(get_db)):

    insurance_provider_query = db.query(models.InsuranceProvider).filter(
        models.InsuranceProvider.id == id)

    insurance_provider = insurance_provider_query.first()


    if insurance_provider == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance provider with id: {id} does not exist")
    
    insurance_provider_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)