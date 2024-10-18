from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel
from datetime import datetime, timezone
from pydantic import BaseModel, Field

class IngredientBase(SQLModel):
    # ingredient_id: Optional[int] = Field(default=None)
    openfoodfacts_id: Optional[str] = Field(max_length=50)
    name: str = Field(max_length=100)


class IngredientCreate(IngredientBase):
    """Schema for creating a new Ingredient."""
    category_id: Optional[int] 
    created_at: Optional[datetime] 
    openfoodfacts_content: Optional[dict]
    updated_at: Optional[datetime]


class IngredientRead(IngredientBase):
    """Schema for reading Ingredient data."""
    ingredient_id: int
    created_at: datetime
    updated_at: datetime

class IngredientUpdate(IngredientBase):
    """Schema for updating an Ingredient."""
    openfoodfacts_content: Optional[dict] = None
    category_id: Optional[int] = None
    updated_at: datetime = None
