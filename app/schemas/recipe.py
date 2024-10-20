from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field

class RecipeBase(SQLModel):
    """Base schema for Recipe."""
    title: str = Field(max_length=255)
    description: Optional[str] = None
    instructions: Optional[str] = None
    prep_time: Optional[int] = Field(default=None, description="Preparation time in minutes")
    cook_time: Optional[int] = Field(default=None, description="Cooking time in minutes")
    servings: Optional[int] = None
    image_url: Optional[str] = Field(default=None, max_length=255)

class RecipeCreate(RecipeBase):
    """Schema for creating a new Recipe."""
    pass  # All fields are inherited from RecipeBase

class RecipeRead(RecipeBase):
    """Schema for reading Recipe data."""
    recipe_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    # Related data
    # ingredients: List["RecipeIngredientRead"] = []
    # user: "UserRead" = None
    # comments: List["CommentRead"] = []
    # likes: List["LikeRead"] = []
    # folders: List["FolderRecipeRead"] = []

class RecipeUpdate(SQLModel):
    """Schema for updating an existing Recipe."""
    title: Optional[str] = Field(default=None, max_length=255)
    description: Optional[str] = None
    instructions: Optional[str] = None
    prep_time: Optional[int] = Field(default=None, description="Preparation time in minutes")
    cook_time: Optional[int] = Field(default=None, description="Cooking time in minutes")
    servings: Optional[int] = None
    image_url: Optional[str] = Field(default=None, max_length=255)
