from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel
from datetime import datetime, timezone
from pydantic import BaseModel, Field

class IngredientBase(SQLModel):
    ingredient_id: Optional[int] = Field(default=None)
    openfoodfacts_id: str = Field(max_length=50)
    name: str = Field(max_length=100)
    standard_name: str = Field(max_length=100)
    category_id: Optional[int] = Field(default=None)
    synonyms: Optional[List[str]] = None
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))


class IngredientCreate(IngredientBase):
    """Schema for creating a new Ingredient."""
    pass  # Inherits all fields from IngredientBase

class IngredientRead(IngredientBase):
    """Schema for reading Ingredient data."""
    ingredient_id: int
    created_at: datetime
    updated_at: datetime

class IngredientUpdate(SQLModel):
    """Schema for updating an Ingredient."""
    openfoodfacts_id: Optional[str] = None
    name: Optional[str] = None
    standard_name: Optional[str] = None
    category_id: Optional[int] = None
    synonyms: Optional[list[str]] = None
