from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(
    prefix="/administrator",
     tags=['Administrators']

)


""" ADMINISTRATOR API """
# Create Administrator


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_administrator(administrator: schemas.AdministratorCreate, db: Session = Depends(get_db)):
    new_administrator = models.Administrator(**administrator.dict())
    db.add(new_administrator)
    db.commit()
    db.refresh(new_administrator)
    return new_administrator

# Read One Administrator


@router.get("/{id}", response_model=schemas.AdministratorResponse)
def get_one_administrator(id: str, db: Session = Depends(get_db)):
    administrator = db.query(models.Administrator).filter(
        models.Administrator.id == id).first()

    if not administrator:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Administrator with id: {id} was not found")
    return administrator

# Read All Administrator


@router.get("/", response_model=List[schemas.AdministratorResponse])
def get_administrator(db: Session = Depends(get_db)):
    administrator = db.query(models.Administrator).all()
    return administrator

# Update Administrator


@router.put("/{id}", response_model=schemas.AdministratorResponse)
def update_administrator(id: str, updated_administrator: schemas.AdministratorCreate, db: Session = Depends(get_db)):

    administrator_query = db.query(models.Administrator).filter(
        models.Administrator.id == id)

    administrator = administrator_query.first()

    if administrator == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Administrator with id: {id} does not exist")

    administrator_query.update(
        updated_administrator.dict(), synchronize_session=False)
    db.commit()
    return administrator_query.first()


# Delete Admission
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_administrator(id: str, db: Session = Depends(get_db)):

    administrator = db.query(models.Administrator).filter(
        models.Administrator.id == id)

    if administrator.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Administrator with id: {id} does not exist")

    administrator.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)