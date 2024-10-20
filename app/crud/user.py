from sqlmodel import Session, select
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from datetime import datetime
from app.utils.security import get_password_hash, verify_password
from typing import Optional

def create_user(db: Session, user_create: UserCreate) -> User:
    """Create a new user with a hashed password."""
    user = User(
        username=user_create.username,
        email=user_create.email,
        password_hash=get_password_hash(user_create.password),
        profile_pic=user_create.profile_pic,
        bio=user_create.bio,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.get(User, user_id)

def get_user_by_username(db: Session, username: str) -> Optional[User]:
    statement = select(User).where(User.username == username)
    return db.exec(statement).first()

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    statement = select(User).where(User.email == email)
    return db.exec(statement).first()

def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.password_hash):
        return None
    return user

def update_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    user_data = user_update.dict(exclude_unset=True)
    if "password" in user_data:
        user_data["password_hash"] = get_password_hash(user_data.pop("password"))
    for key, value in user_data.items():
        setattr(user, key, value)
    user.updated_at = datetime.utcnow()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int) -> bool:
    user = get_user_by_id(db, user_id)
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True
