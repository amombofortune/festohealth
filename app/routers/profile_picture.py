from fastapi import Depends, File, UploadFile, status, APIRouter, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from ..database import get_db
from .. import oauth2


router = APIRouter(
     prefix="/profile",
     tags=['profile']


)

def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.id == user_id).first()

@router.post("/profile", status_code=status.HTTP_200_OK)
def upload_image(
    user_id: str,
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    if current_user.id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")

    user = get_user_by_id(user_id, db)  # Retrieve the user from the database

    # Process the uploaded image
    image_data = image.file.read()  # Read the binary image data

    # Update the user's image in the database
    user.image = image_data
    db.commit()

    return {"message": "Image uploaded successfully"}

