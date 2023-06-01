from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import oauth2


router = APIRouter(
     prefix="/lab_test",
     tags=['Lab Test']


)


""" LAB TEST APIs """
# Create lab test
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_lab_test(lab_test: schemas.LabTestCreate, db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):
    new_lab_test = models.LabTest(user_id= current_user.id, **lab_test.dict())
    db.add(new_lab_test)
    db.commit()
    db.refresh(new_lab_test)
    return new_lab_test

# Read one lab test


@router.get("/{id}", response_model=schemas.LabTestResponse)
def get_lab_test(id: int, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):
    lab_test = db.query(models.LabTest).filter(models.LabTest.id == id).first()

    if not lab_test:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test with id: {id} was not found")
    return lab_test

# Read All lab tests
@router.get("/", response_model=List[schemas.LabTestResponse])
def get_lab_tests(db: Session = Depends(get_db),
                  current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    lab_tests = db.query(models.LabTest)\
    .filter(models.LabTest.user_id == current_user.id)\
    .filter(models.LabTest.test_name.ilike(f'%{search}%'))\
    .limit(limit)\
    .offset(skip)\
    .all()
    return lab_tests

# Update lab tests
@router.put("/{id}", response_model=schemas.LabTestResponse)
def update_lab_test(id: int, updated_lab_test: schemas.LabTestCreate, db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):

    lab_test_query = db.query(models.LabTest).filter(models.LabTest.id == id)

    lab_test = lab_test_query.first()

    if lab_test == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test with id: {id} does not exist")
    
    if lab_test.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    lab_test_query.update(updated_lab_test.dict(), synchronize_session=False)
    db.commit()
    return lab_test_query.first()


# Delete lab test
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lab_test(id: int, db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):

    lab_test_query = db.query(models.LabTest).filter(models.LabTest.id == id)

    lab_test = lab_test_query.first()


    if lab_test == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab test with id: {id} does not exist")
    
    if lab_test.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    lab_test_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)