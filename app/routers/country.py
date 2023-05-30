from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/country",
     tags=['Country']


)



""" COUNTRY APIs"""
# Create Country


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db),
                    user_id: int = Depends(oauth2.get_current_user)):
    new_country = models.Country(**country.dict())
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country

# Read One Country


@router.get("/{id}", response_model=schemas.CountryResponse)
def get_country(id: int, db: Session = Depends(get_db),
                user_id: int = Depends(oauth2.get_current_user)):
    country = db.query(models.Country).filter(models.Country.id == id).first()

    if not country:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Country with id: {id} was not found")
    return country

# Read All Countries


@router.get("/", response_model=List[schemas.CountryResponse])
def get_country(db: Session = Depends(get_db),
                user_id: int = Depends(oauth2.get_current_user)):
    country = db.query(models.Country).all()
    return country

# Update Country


@router.put("/{id}", response_model=schemas.CountryResponse)
def update_country(id: int, updated_country: schemas.CountryCreate, db: Session = Depends(get_db),
                   user_id: int = Depends(oauth2.get_current_user)):

    country_query = db.query(models.Country).filter(models.Country.id == id)

    country = country_query.first()

    if country == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Country with id: {id} does not exist")

    country_query.update(updated_country.dict(), synchronize_session=False)
    db.commit()
    return country_query.first()


# Delete country
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_country(id: int, db: Session = Depends(get_db),
                   user_id: int = Depends(oauth2.get_current_user)):

    country = db.query(models.Country).filter(models.Country.id == id)

    if country.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Country with id: {id} does not exist")

    country.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
