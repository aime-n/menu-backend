from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta

from app.database import get_session
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.crud.user import (
    create_user,
    get_user_by_username,
    get_user_by_email,
    authenticate_user,
    update_user,
    delete_user,
)
from app.utils.auth import (
    create_access_token, 
    ACCESS_TOKEN_EXPIRE_MINUTES, 
    get_current_user
)
from app.models.user import User
import logging

logging.getLogger('passlib').setLevel(logging.ERROR)

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

@router.post("/register", response_model=UserRead, status_code=201)
def register(user_create: UserCreate, db: Session = Depends(get_session)):
    if get_user_by_username(db, user_create.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    if get_user_by_email(db, user_create.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = create_user(db, user_create)
    return new_user

@router.post("/token")
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.user_id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserRead)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserRead)
def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session),
):
    updated_user = update_user(db, current_user.user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/me", status_code=204)
def delete_current_user(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_session)
):
    success = delete_user(db, current_user.user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return None
