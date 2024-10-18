from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel
from datetime import datetime, timezone
from pydantic import BaseModel, Field

class IngredientBase(SQLModel):
    # ingredient_id: Optional[int] = Field(default=None)
    openfoodfacts_id: Optional[str] = Field(max_length=50)
    openfoodfacts_content: Optional[dict]
    name: str = Field(max_length=100)
    category_id: Optional[int] 
    created_at: Optional[datetime] 


class IngredientCreate(IngredientBase):
    """Schema for creating a new Ingredient."""
    updated_at: Optional[datetime] = None


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
    updated_at: datetime
    category_id: Optional[int] = None
