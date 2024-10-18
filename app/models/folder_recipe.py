# from __future__ import annotations
# from typing import Optional, TYPE_CHECKING
# from sqlmodel import Field, SQLModel, Relationship
# 

# if TYPE_CHECKING:
#     from .folder import Folder
#     from .recipe import Recipe

    
# class FolderRecipe(SQLModel, table=True):
#     """SQLModel for the folder_recipes table."""
#     __tablename__ = "folder_recipes"
#     __table_args__ = {"schema": "recipes_db"}

#     folder_id: int = Field(foreign_key="recipes_db.folders.folder_id", primary_key=True)
#     recipe_id: int = Field(foreign_key="recipes_db.recipes.recipe_id", primary_key=True)

#     # Relationships
#     folder: Optional["Folder"]] = Relationship(back_populates="recipes")
#     recipe: Optional["Recipe"]] = Relationship(back_populates="folders")
