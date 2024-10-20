from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    """SQLModel for the users table."""
    __tablename__ = "users"

    user_id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(max_length=50, unique=True, nullable=False)
    email: str = Field(max_length=100, unique=True, nullable=False)
    password_hash: str = Field(max_length=255, nullable=False)
    profile_pic: Optional[str] = Field(max_length=255)
    bio: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)  
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)  

    # Relationships
    followers: List["Follow"] = Relationship(
        back_populates="followed",
        sa_relationship_kwargs={
            "primaryjoin": "User.user_id == Follow.followed_id"
        }
    )
    following: List["Follow"] = Relationship(
        back_populates="follower",
        sa_relationship_kwargs={
            "primaryjoin": "User.user_id == Follow.follower_id"
        }
    )
    
    # Other relationships
    recipes: List["Recipe"] = Relationship(back_populates="user")
    ingredients: List["UserInventory"] = Relationship(back_populates="user")
    comments: List["Comment"] = Relationship(back_populates="user")
    likes: List["Like"] = Relationship(back_populates="user")
    folders: List["Folder"] = Relationship(back_populates="user")
    preferences: List["UserPreference"] = Relationship(back_populates="user")
