from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, models
from .database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    user_id = data.get("id")
    user_type = data.get("user_type")
    registration_form_completed = data.get("registration_form_completed")

    if user_id:
        to_encode["user_id"] = user_id
    if user_type:
        to_encode["user_type"] = user_type
    if registration_form_completed is not None:
        to_encode["registration_form_completed"] = registration_form_completed

    expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt




def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id: str = payload.get("user_id")
        user_type: str = payload.get("user_type")
        registration_form_completed: bool = payload.get("registration_form_completed")

        if user_id is None:
            raise credentials_exception

        token_data = {
            "id": user_id,
            "user_type": user_type,
            "registration_form_completed": registration_form_completed,
        }

    except JWTError: 
        raise credentials_exception

    return token_data



def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        token_data = verify_access_token(token, credentials_exception)
    except HTTPException as e:
        if e.status_code == status.HTTP_401_UNAUTHORIZED:
            # Token expired
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        else:
            # Other token verification error
            raise e

    user_id = token_data["id"]
    user_type = token_data.get("user_type", None)  # Get user_type from token_data (can be None if not provided)
    registration_form_completed = token_data.get("registration_form_completed", False)  # Get registration_form_completed from token_data (default to False if not provided)

    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise credentials_exception

    user.user_type = user_type
    user.registration_form_completed = registration_form_completed

    return user




"""
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
"""

"""
def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = {"id": id}

    except JWTError: 
        raise credentials_exception

    return token_data
 """


"""
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        token_data = verify_access_token(token, credentials_exception)
    except HTTPException as e:
        if e.status_code == status.HTTP_401_UNAUTHORIZED:
            # Token expired
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        else:
            # Other token verification error
            raise e

    user = db.query(models.User).filter(models.User.id == token_data["id"]).first()

    return user
"""