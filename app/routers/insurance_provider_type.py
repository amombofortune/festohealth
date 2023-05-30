from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/insurance_provider_type",
     tags=['Insurance Provider Type']


)



""" INSURANCE PROVIDER TYPE APIs """
# Create insurance provider type


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_insurance_provider_type(insurance_provider_type: schemas.InsuranceProviderTypeCreate, db: Session = Depends(get_db),
                                   user_id: int = Depends(oauth2.get_current_user)):
    new_insurance_provider_type = models.InsuranceProviderType(
        **insurance_provider_type.dict())
    db.add(new_insurance_provider_type)
    db.commit()
    db.refresh(new_insurance_provider_type)
    return new_insurance_provider_type

# Read one insurance provider type


@router.get("/{id}", response_model=schemas.InsuranceProviderTypeResponse)
def get_insurance_provider_type(id: int, db: Session = Depends(get_db),
                                user_id: int = Depends(oauth2.get_current_user)):
    insurance_provider_type = db.query(models.InsuranceProviderType).filter(
        models.InsuranceProviderType.id == id).first()

    if not insurance_provider_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance provider type with id: {id} was not found")
    return insurance_provider_type

# Read All insurance provider type


@router.get("/", response_model=List[schemas.InsuranceProviderTypeResponse])
def get_insurance_provider_type(db: Session = Depends(get_db),
                                user_id: int = Depends(oauth2.get_current_user)):
    insurance_provider_type = db.query(models.InsuranceProviderType).all()
    return insurance_provider_type

# Update insurance provider


@router.put("/{id}", response_model=schemas.InsuranceProviderTypeResponse)
def update_insurance_provider_type(id: int, updated_insurance_provider_type: schemas.InsuranceProviderTypeCreate, db: Session = Depends(get_db),
                                   user_id: int = Depends(oauth2.get_current_user)):

    insurance_provider_type_query = db.query(models.InsuranceProviderType).filter(
        models.InsuranceProviderType.id == id)

    insurance_provider_type = insurance_provider_type_query.first()

    if insurance_provider_type == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance provider type with id: {id} does not exist")

    insurance_provider_type_query.update(
        updated_insurance_provider_type.dict(), synchronize_session=False)
    db.commit()
    return insurance_provider_type_query.first()


# Delete insurance provider
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_insurance_provider_type(id: int, db: Session = Depends(get_db),
                                   user_id: int = Depends(oauth2.get_current_user)):

    insurance_provider_type = db.query(models.InsuranceProviderType).filter(
        models.InsuranceProviderType.id == id)

    if insurance_provider_type.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insurance provider type with id: {id} does not exist")

    insurance_provider_type.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
