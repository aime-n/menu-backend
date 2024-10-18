from typing import List, Optional
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel


class Ingredient(SQLModel, table=True):
    __tablename__ = "ingredients"
    ingredient_id: Optional[int] = Field(default=None, primary_key=True)
    openfood_facts_id: Optional[str] = None
    name: str
    standard_name: Optional[str] = None
    category_id: Optional[int] = Field(default=None, foreign_key="categories.category_id")
    created_at: datetime
    updated_at: datetime

    # Relationship
    category: Optional["Category"] = Relationship(back_populates="ingredients")
