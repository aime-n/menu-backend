from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


    
class RecipeIngredient(SQLModel, table=True):
    """SQLModel for the recipe_ingredients table."""
    __tablename__ = "recipe_ingredients"

    recipe_id: Optional[int] = Field(
        default=None, foreign_key="recipes.recipe_id", primary_key=True)
    ingredient_id: Optional[int] = Field(
        default=None, foreign_key="ingredients.ingredient_id", primary_key=True)

    # Relationships
    recipe: Optional["Recipe"] = Relationship(back_populates="ingredients")
    ingredient: Optional["Ingredient"] = Relationship(back_populates="recipe_associations")
