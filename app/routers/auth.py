from .. import models, schemas, utils
from .. import oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import HTTPException, status, Depends,APIRouter
from fastapi.responses import RedirectResponse
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.schemas import  Token



router = APIRouter(tags=['Authentication'])

"""
@router.post("/login", response_model=Token)
def login_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id, "user_type": user.user_type})


    # Create a Token response with the required fields, including the first_login flag
    token_response = Token(
        access_token=access_token,
        token_type="bearer",
        user_id=user.id,
        email=user.email,
        user_type=user.user_type
    )

    # Set the access token as an HTTP-only cookie
    response = JSONResponse(content=token_response.dict())
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="None"
    )

    return response
"""
@router.post("/login", response_model=Token)
def login_user(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    data = {
        "id": user.id,
        "user_type": user.user_type,
        "registration_form_completed": user.registration_form_completed,
    }
    access_token = oauth2.create_access_token(data)

    # Create a Token response with the required fields
    token_response = Token(
        access_token=access_token,
        token_type="bearer",
        user_id=user.id,
        email=user.email,
        user_type=user.user_type,
        registration_form_completed=user.registration_form_completed,
    )

    # Set the access token as an HTTP-only cookie and return the token response
    response = JSONResponse(content=token_response.dict())
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="None"
    )

    return response







@router.post("/logout")
def logout_user(response: Response):
    # Clear the access token cookie
    response.delete_cookie(key="access_token")

    # Return a response indicating successful logout
    return {"message": "Logout successful"}


