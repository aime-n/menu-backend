from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field
from pydantic import EmailStr, constr

class UserCreate(SQLModel):
    username: str = Field(max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)
    profile_pic: Optional[str] = None
    bio: Optional[str]

class UserRead(SQLModel):
    user_id: int
    username: str
    email: EmailStr
    profile_pic: Optional[str]
    bio: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class UserUpdate(SQLModel):
    username: Optional[str] = Field(default=None, max_length=50)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(min_length=8, default=None)
    profile_pic: Optional[str] = None
    bio: Optional[str] = None

