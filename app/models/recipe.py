# from __future__ import annotations
# from typing import Optional, List, TYPE_CHECKING
# from datetime import datetime, timezone
# from sqlmodel import Field, SQLModel, Relationship
# from sqlalchemy.orm import Mapped, relationship

# if TYPE_CHECKING:
#     from .user import User
#     from .recipe_ingredient import RecipeIngredient
#     from .comment import Comment
#     from .like import Like
#     from .folder_recipe import FolderRecipe

# class Recipe(SQLModel, table=True):
#     """SQLModel for the recipes table."""
#     __tablename__ = "recipes"
#     __table_args__ = {"schema": "recipes_db"}

#     recipe_id: Optional[int] = Field(default=None, primary_key=True)
#     user_id: int = Field(foreign_key="recipes_db.users.user_id")
#     title: str = Field(max_length=255)
#     description: Optional[str] = None
#     instructions: Optional[str] = None
#     prep_time: Optional[int] = None  # in minutes
#     cook_time: Optional[int] = None  # in minutes
#     servings: Optional[int] = None
#     image_url: Optional[str] = Field(max_length=255)
#     created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
#     updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))

#     # Relationships
#     user: Mapped[Optional["User"]] = relationship(back_populates="recipes")
#     ingredients: Mapped[List["RecipeIngredient"]] = relationship(back_populates="recipe")
#     comments: Mapped[List["Comment"]] = relationship(back_populates="recipe")
#     likes: Mapped[List["Like"]] = relationship(back_populates="recipe")
#     folders: Mapped[List["FolderRecipe"]] = relationship(back_populates="recipe")

#     # user: Optional["User"] = relationship(back_populates="recipes")
#     # ingredients: List["RecipeIngredient"] = relationship(back_populates="recipe")
#     # comments: List["Comment"] = relationship(back_populates="recipe")
#     # likes: List["Like"] = relationship(back_populates="recipe")
#     # folders: List["FolderRecipe"] = relationship(back_populates="recipe")