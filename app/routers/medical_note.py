from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/medical_note",
     tags=['Medical Note']


)


""" MEDICAL NOTES APIs """
# Create medical notes


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_medical_note(medical_note: schemas.MedicalNoteCreate, db: Session = Depends(get_db),
                        user_id: int = Depends(oauth2.get_current_user)):
    new_medical_note = models.MedicalNote(**medical_note.dict())
    db.add(new_medical_note)
    db.commit()
    db.refresh(new_medical_note)
    return new_medical_note

# Read one medical note


@router.get("/{id}", response_model=schemas.MedicalNoteResponse)
def get_medical_note(id: int, db: Session = Depends(get_db),
                     user_id: int = Depends(oauth2.get_current_user)):
    medical_note = db.query(models.MedicalNote).filter(
        models.MedicalNote.id == id).first()

    if not medical_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical note with id: {id} was not found")
    return medical_note

# Read All medical notes


@router.get("/", response_model=List[schemas.MedicalNoteResponse])
def get_medical_note(db: Session = Depends(get_db),
                     user_id: int = Depends(oauth2.get_current_user)):
    medical_notes = db.query(models.MedicalNote).all()
    return medical_notes

# Update medical note


@router.put("/{id}", response_model=schemas.MedicalNoteResponse)
def update_medical_note(id: int, updated_medical_note: schemas.MedicalNoteCreate, db: Session = Depends(get_db),
                        user_id: int = Depends(oauth2.get_current_user)):

    medical_note_query = db.query(models.MedicalNote).filter(
        models.MedicalNote.id == id)

    medical_note = medical_note_query.first()

    if medical_note == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical note with id: {id} does not exist")

    medical_note_query.update(
        updated_medical_note.dict(), synchronize_session=False)
    db.commit()
    return medical_note_query.first()


# Delete medical note
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_note(id: int, db: Session = Depends(get_db),
                        user_id: int = Depends(oauth2.get_current_user)):

    medical_note = db.query(models.MedicalNote).filter(
        models.MedicalNote.id == id)

    if medical_note.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical note with id: {id} does not exist")

    medical_note.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)