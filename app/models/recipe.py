from typing import Optional, List
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship




class Recipe(SQLModel, table=True):
    """SQLModel for the recipes table."""
    __tablename__ = "recipes"

    recipe_id: Optional[int] = Field(default=None, primary_key=True)
    # user_id: int = Field(foreign_key="users.user_id")
    title: str = Field(max_length=255)
    description: Optional[str] = None
    instructions: Optional[str] = None
    prep_time: Optional[int] = None  
    cook_time: Optional[int] = None  
    servings: Optional[int] = None
    image_url: Optional[str] = Field(max_length=255)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))

    # Relationships
    ingredients: List["RecipeIngredient"] = Relationship(back_populates="recipe")





    # user: Optional["User"]] = Relationship(back_populates="recipes")
    # ingredients: List["RecipeIngredient"]] = Relationship(back_populates="recipe")
    # comments: List["Comment"]] = Relationship(back_populates="recipe")
    # likes: List["Like"]] = Relationship(back_populates="recipe")
    # folders: List["FolderRecipe"]] = Relationship(back_populates="recipe")



    # user: Optional["User"] = Relationship(back_populates="recipes")
    # comments: List["Comment"] = Relationship(back_populates="recipe")
    # likes: List["Like"] = Relationship(back_populates="recipe")
    # folders: List["FolderRecipe"] = Relationship(back_populates="recipe")