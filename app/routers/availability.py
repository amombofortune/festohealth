from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from .. import oauth2
from typing import List, Optional

router = APIRouter(
    prefix="/availability",
     tags=['Availability']

)

""" AVAILABILITY API """
# Create Availability
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_availability(availability: schemas.AvailabilityCreate, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):

    start_time = availability.start_time
    end_time = availability.end_time

    if len(start_time) != len(end_time):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Number of start times and end times should be the same"
        )

    # Iterate over the start times and end times
    for start_time, end_time in zip(start_time, end_time):
        new_availability = models.Availability(
            user_id=current_user.id,
            date=availability.date,
            start_time=start_time,
            end_time=end_time
        )
        db.add(new_availability)

    db.commit()
    db.refresh(new_availability)

    return new_availability




# Read One availability
@router.get("/{id}", response_model=schemas.AvailabilityResponse)
def get_one_availability(id: int, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read availability"
        )
    
    availability = db.query(models.Availability).filter(
        models.Availability.id == id).first()

    if not availability:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"availability with id: {id} was not found")
    return availability

# Read All availability
@router.get("/", response_model=List[schemas.AvailabilityResponse])
def get_availability(db: Session = Depends(get_db),
                  current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
    # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital", "patient"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors, hospitals or patients can read availability"
        )

    availability = db.query(models.Availability).all()
    return availability



# Update availability
@router.put("/{id}", response_model=schemas.AvailabilityResponse)
def update_availability(id: int, updated_availability: schemas.AvailabilityCreate, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "doctor" or "hospital" or "patient" role
    if current_user.user_type not in ["doctor", "hospital"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors or hospitals can update availability"
        )

    availability_query = db.query(models.Availability).filter(
        models.Availability.id == id)

    availability = availability_query.first()

    if availability == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"availability with allergy_id: {id} does not exist")
    
    if availability.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    availability_query.update(updated_availability.dict(), synchronize_session=False)
    db.commit()
    return availability_query.first()


# Delete availability
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_availability(id: int, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    
    # Check if the current user has the "patient" role
    if current_user.user_type != "patient":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only patients can delete availability"
        )

    availability_query = db.query(models.Availability).filter(models.Availability.id == id)

    availability = availability_query.first()

    if availability == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Availability with id: {id} does not exist")
    
    if availability.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    availability_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)