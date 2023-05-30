from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
import bcrypt
from typing import List

router = APIRouter(
     prefix="/users",
     tags=['Users']

)

""" USERS APIs"""
# Create user account


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    #hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Read single user account


@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} was not found")
    return user

# Read All user account


@router.get("/", response_model=List[schemas.UserResponse])
def get_user_accounts(db: Session = Depends(get_db)):
    user_accounts = db.query(models.User).all()
    return user_accounts

# Update user account


@router.put("/{id}", response_model=schemas.UserResponse)
def update_user_account(id: str, updated_user_account: schemas.UserCreate, db: Session = Depends(get_db)):

    user_account_query = db.query(models.User).filter(models.User.id == id)

    user_account = user_account_query.first()

    if user_account == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User account with id: {id} does not exist")

    user_account_query.update(
        updated_user_account.dict(), synchronize_session=False)
    db.commit()
    return user_account_query.first()


# Delete user account
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_account(id: str, db: Session = Depends(get_db)):

    user_account = db.query(models.User).filter(models.User.id == id)

    if user_account.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User account with id: {id} does not exist")

    user_account.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)




