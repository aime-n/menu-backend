# from __future__ import annotations
# from typing import Optional, List, TYPE_CHECKING
# from datetime import datetime, timezone
# from sqlmodel import Field, SQLModel, Relationship
# from sqlalchemy.orm import Mapped, relationship

# if TYPE_CHECKING:
#     from .recipe import Recipe
#     from .comment import Comment
#     from .like import Like
#     from .folder import Folder
#     from .user_ingredient import UserIngredient
#     from .user_preference import UserPreference
#     from .follow import Follow

    
# class User(SQLModel, table=True):
#     """SQLModel for the users table."""
#     __tablename__ = "users"
#     __table_args__ = {"schema": "recipes_db"}

#     user_id: Optional[int] = Field(default=None, primary_key=True)
#     username: str = Field(max_length=50, unique=True, nullable=False)
#     email: str = Field(max_length=100, unique=True, nullable=False)
#     password_hash: str = Field(max_length=255, nullable=False)
#     profile_pic: Optional[str] = Field(max_length=255)
#     bio: Optional[str] = None
#     created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
#     updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))

#     # Relationships
#     recipes: Mapped[List["Recipe"]] = relationship(back_populates="user")
#     comments: Mapped[List["Comment"]] = relationship(back_populates="user")
#     likes: Mapped[List["Like"]] = relationship(back_populates="user")
#     folders: Mapped[List["Folder"]] = relationship(back_populates="user")
#     ingredients: Mapped[List["UserIngredient"]] = relationship(back_populates="user")
#     preferences: Mapped[List["UserPreference"]] = relationship(back_populates="user")
#     followers: Mapped[List["Follow"]] = relationship(back_populates="followed")
#     following: Mapped[List["Follow"]] = relationship(back_populates="follower")
#     # recipes: List["Recipe"] = relationship(back_populates="user")
#     # comments: List["Comment"] = relationship(back_populates="user")
#     # likes: List["Like"] = relationship(back_populates="user")
#     # folders: List["Folder"] = relationship(back_populates="user")
#     # ingredients: List["UserIngredient"] = relationship(back_populates="user")
#     # preferences: List["UserPreference"] = relationship(back_populates="user")
