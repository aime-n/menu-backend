
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class FolderRecipe(SQLModel, table=True):
    """SQLModel for the folder_recipes table."""
    __tablename__ = "folder_recipes"

    folder_id: int = Field(foreign_key="folders.folder_id", primary_key=True)
    recipe_id: int = Field(foreign_key="recipes.recipe_id", primary_key=True)

    # Relationships
    folder: Optional["Folder"] = Relationship(back_populates="recipes")
    recipe: Optional["Recipe"] = Relationship(back_populates="folders")
