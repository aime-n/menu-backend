# from __future__ import annotations
# from typing import Optional, TYPE_CHECKING
# from sqlmodel import Field, SQLModel, Relationship
# from sqlalchemy.orm import Mapped, relationship

# if TYPE_CHECKING:
#     from .recipe import Recipe
#     from .ingredient import Ingredient

    
# class RecipeIngredient(SQLModel, table=True):
#     """SQLModel for the recipe_ingredients table."""
#     __tablename__ = "recipe_ingredients"
#     __table_args__ = {"schema": "recipes_db"}

#     recipe_id: Optional[int] = Field(
#         default=None, foreign_key="recipes_db.recipes.recipe_id", primary_key=True
#     )
#     ingredient_id: Optional[int] = Field(
#         default=None, foreign_key="recipes_db.ingredients.ingredient_id", primary_key=True
#     )

#     # Relationships
#     recipe: Mapped[Optional["Recipe"]] = relationship(back_populates="ingredients")
#     ingredient: Mapped[Optional["Ingredient"]] = relationship(back_populates="recipe_associations")
