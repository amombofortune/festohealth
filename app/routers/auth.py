from .. import models, schemas, utils
from . import oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import FastAPI, HTTPException, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=['Authentication'])


@router.post("/login", response_model=schemas.Token)
def login_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid credentials")
    
    #create a token
    #return token

    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}


