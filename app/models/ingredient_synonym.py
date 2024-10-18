# from __future__ import annotations
# from typing import Optional, TYPE_CHECKING
# from datetime import datetime, timezone
# from sqlmodel import Field, SQLModel, Relationship
# 

# if TYPE_CHECKING:
#     from .ingredient import Ingredient

# class IngredientSynonym(SQLModel, table=True):
#     """SQLModel for the ingredient_synonyms table."""
#     __tablename__ = "ingredient_synonyms"
#     __table_args__ = {"schema": "recipes_db"}

#     synonym_id: Optional[int] = Field(default=None, primary_key=True)
#     ingredient_id: int = Field(foreign_key="recipes_db.ingredients.ingredient_id")
#     synonym: str = Field(max_length=100)
#     created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
#     updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))

#     # Relationships
#     ingredient: Optional["Ingredient"]] = Relationship(back_populates="synonyms_list")
