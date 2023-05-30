from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from . import oauth2
from typing import List

router = APIRouter(
    prefix="/admission",
     tags=['Admission']

)

""" ADMISSION API """
# Create Admission
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_admission(admission: schemas.AdmissionCreate, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
    new_admission = models.Admission(user_id= current_user.id, **admission.dict())
    db.add(new_admission)
    db.commit()
    db.refresh(new_admission)
    return new_admission

# Read One Admission
@router.get("/{id}", response_model=schemas.AdmissionResponse)
def get_one_admission(id: int, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    admission = db.query(models.Admission).filter(
        models.Admission.id == id).first()

    if not admission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admission with id: {id} was not found")
    return admission

# Read All Admission
@router.get("/", response_model=List[schemas.AdmissionResponse])
def get_admission(db: Session = Depends(get_db),
                  current_user: int = Depends(oauth2.get_current_user)):
    print(current_user.email)

    admission = db.query(models.Admission).filter(models.Admission.user_id == current_user.id).all()

    if admission.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")
    return admission



# Update Admission
@router.put("/{id}", response_model=schemas.AdmissionResponse)
def update_admission(id: int, updated_admission: schemas.AdmissionCreate, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):

    admission_query = db.query(models.Admission).filter(
        models.Admission.id == id)

    admission = admission_query.first()

    if admission == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admission with allergy_id: {id} does not exist")
    
    if admission.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    admission_query.update(updated_admission.dict(), synchronize_session=False)
    db.commit()
    return admission_query.first()


# Delete Admission
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_admission(id: int, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):

    admission_query = db.query(models.Admission).filter(models.Admission.id == id)

    admission = admission_query.first()

    if admission == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admission with id: {id} does not exist")
    
    if admission.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    admission_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)