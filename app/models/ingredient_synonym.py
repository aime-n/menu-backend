
from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship


class IngredientSynonym(SQLModel, table=True):
    """SQLModel for the ingredient_synonyms table."""
    __tablename__ = "ingredient_synonyms"
    

    synonym_id: Optional[int] = Field(default=None, primary_key=True)
    ingredient_id: int = Field(foreign_key="ingredients.ingredient_id")
    synonym: str = Field(max_length=100)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    # Relationships
    ingredient: Optional["Ingredient"] = Relationship(back_populates="synonyms_list")