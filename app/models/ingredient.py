from typing import List, Optional
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy.dialects.postgresql import JSONB


class Ingredient(SQLModel, table=True):
    __tablename__ = "ingredients"

    ingredient_id: Optional[int] = Field(default=None, primary_key=True)
    openfoodfacts_id: Optional[str] = None
    openfoodfacts_content: Optional[dict] = Field(default=None, sa_type=JSONB, nullable=False)
    name: str
    category_id: Optional[int] = Field(default=None, foreign_key="categories.category_id")
    created_at: datetime
    updated_at: Optional[datetime] = Field(default=None, nullable=True)  

    # Relationship
    category: Optional["Category"] = Relationship(back_populates="ingredients")
    recipe_associations: List["RecipeIngredient"] = Relationship(back_populates="ingredient")
    user_associations: List["UserInventory"] = Relationship(back_populates="ingredient")
    synonyms_list: List["IngredientSynonym"] = Relationship(back_populates="ingredient")
