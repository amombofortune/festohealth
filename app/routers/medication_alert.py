from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from . import oauth2


router = APIRouter(
     prefix="/medical_alert",
     tags=['Medication Alert']


)


""" MEDICATION ALERTS APIs """
# Create medication alerts
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_medical_alert(medication_alert: schemas.MedicationAlertCreate, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):
    new_medical_alert = models.MedicationAlert(user_id= current_user.id, **medication_alert.dict())
    db.add(new_medical_alert)
    db.commit()
    db.refresh(new_medical_alert)
    return new_medical_alert

# Read one medical alert


@router.get("/{id}", response_model=schemas.MedicationAlertResponse)
def get_medical_alert(id: int, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    medical_alert = db.query(models.MedicationAlert).filter(
        models.MedicationAlert.id == id).first()

    if not medical_alert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical alert with id: {id} was not found")
    return medical_alert

# Read All medical alerts


@router.get("/", response_model=List[schemas.MedicationAlertResponse])
def get_medical_alerts(db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):
    medical_alerts = db.query(models.MedicationAlert).filter(models.MedicationAlert.user_id == current_user.id).all()
    return medical_alerts

# Update medical alerts


@router.put("/{id}", response_model=schemas.MedicationAlertResponse)
def update_medical_alert(id: int, updated_medical_alert: schemas.MedicationAlertCreate, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):

    medical_alert_query = db.query(models.MedicationAlert).filter(
        models.MedicationAlert.id == id)

    medical_alert = medical_alert_query.first()

    if medical_alert == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical alert with id: {id} does not exist")
    
    if medical_alert.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medical_alert_query.update(
        updated_medical_alert.dict(), synchronize_session=False)
    db.commit()
    return medical_alert_query.first()


# Delete medical alert
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_alert(id: int, db: Session = Depends(get_db),
                         current_user: int = Depends(oauth2.get_current_user)):

    medical_alert_query = db.query(models.MedicationAlert).filter(
        models.MedicationAlert.id == id)
    
    medical_alert = medical_alert_query.first()


    if medical_alert == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Medical alert with id: {id} does not exist")
    
    if medical_alert.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    medical_alert_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)