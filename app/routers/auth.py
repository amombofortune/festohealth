from .. import models, schemas, utils
from .. import oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import HTTPException, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter(tags=['Authentication'])

"""
@router.post("/login", response_model=schemas.Token)
def login_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()


    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
"""


@router.post("/login")
def login_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    
    # Create a JSON response with the access token
    response = JSONResponse(content={"access_token": access_token, "token_type": "bearer"})
    
    # Set the access token as an HTTP-only cookie
    response.set_cookie(key="access_token", value=access_token, httponly=True, secure=True, samesite="None")
    
    return response


@router.post("/logout")
def logout_user(response: Response):
    # Clear the access token cookie
    response.delete_cookie(key="access_token")

    # Return a response indicating successful logout
    return {"message": "Logout successful"}


