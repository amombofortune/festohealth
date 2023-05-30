from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/insurance_provider",
     tags=['Insurance Provider']


)


""" INSURANCE PROVIDER APIs """
# Create insurance providers

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_insurance_provider(insurance_provider: schemas.InsuranceProviderCreate, db: Session = Depends(get_db),
                             current_user: int = Depends(oauth2.get_current_user)):
    new_insurance_provider = models.InsuranceProvider(user_id= current_user.id, 
        **insurance_provider.dict())
    db.add(new_insurance_provider)
    db.commit()
    db.refresh(new_insurance_provider)
    return new_insurance_provider

# Read one insurance provider


@router.get("/{id}", response_model=schemas.InsuranceProviderResponse)
def get_insurance_provider(id: str, db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):
    insurance_provider = db.query(models.InsuranceProvider).filter(
        models.InsuranceProvider.id == id).first()

    if not insurance_provider:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance provider with id: {id} was not found")
    return insurance_provider

# Read All insurance providers


@router.get("/", response_model=List[schemas.InsuranceProviderResponse])
def get_insurance_provider(db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):
    insurance_provider = db.query(models.InsuranceProvider).all()
    return insurance_provider

# Update insurance provider


@router.put("/{id}", response_model=schemas.InsuranceProviderResponse)
def update_insurance_provider(id: str, updated_insurance_company: schemas.InsuranceProviderCreate, db: Session = Depends(get_db),
                              current_user: int = Depends(oauth2.get_current_user)):

    insurance_provider_query = db.query(models.InsuranceProvider).filter(
        models.InsuranceProvider.id == id)

    insurance_provider = insurance_provider_query.first()

    if insurance_provider == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance company with id: {id} does not exist")

    if insurance_provider.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    insurance_provider_query.update(
        updated_insurance_company.dict(), synchronize_session=False)
    db.commit()
    return insurance_provider_query.first()


# Delete insurance provider
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_insurance_provider(id: str, db: Session = Depends(get_db),
                              current_user: int = Depends(oauth2.get_current_user)):

    insurance_provider_query = db.query(models.InsuranceProvider).filter(
        models.InsuranceProvider.id == id)

    insurance_provider = insurance_provider_query.first()


    if insurance_provider == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance provider with id: {id} does not exist")
    
    if insurance_provider.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    insurance_provider_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)