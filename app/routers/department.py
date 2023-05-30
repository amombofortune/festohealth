from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/department",
     tags=['Department']


)


""" DEPARTMENT APIs"""
# Create Department


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db),
                      user_id: int = Depends(oauth2.get_current_user)):
    new_department = models.Department(**department.dict())
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department

# Read One Department


@router.get("/{id}", response_model=schemas.DepartmentResponse)
def get_department(id: int, db: Session = Depends(get_db),
                   user_id: int = Depends(oauth2.get_current_user)):
    department = db.query(models.Department).filter(
        models.Department.id == id).first()

    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department with id: {id} was not found")
    return department

# Read All Department


@router.get("/", response_model=List[schemas.DepartmentResponse])
def get_department(db: Session = Depends(get_db),
                   user_id: int = Depends(oauth2.get_current_user)):
    department = db.query(models.Department).all()
    return department

# Update Department


@router.put("/{id}", response_model=schemas.DepartmentResponse)
def update_department(id: int, updated_department: schemas.DepartmentCreate, db: Session = Depends(get_db),
                      user_id: int = Depends(oauth2.get_current_user)):

    department_query = db.query(models.Department).filter(
        models.Department.id == id)

    department = department_query.first()

    if department == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department with id: {id} does not exist")

    department_query.update(updated_department.dict(),
                            synchronize_session=False)
    db.commit()
    return department_query.first()


# Delete Department
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_department(id: int, db: Session = Depends(get_db),
                      user_id: int = Depends(oauth2.get_current_user)):

    department = db.query(models.Department).filter(models.Department.id == id)

    if department.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department with id: {id} does not exist")

    department.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)