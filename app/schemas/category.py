from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime

# Base schema for shared attributes
class CategoryBase(SQLModel):
    name: str
    parent_id: Optional[int] = None

# Schema for creating a category
class CategoryCreate(CategoryBase):
    created_at: datetime
    updated_at: Optional[datetime] = None

# Schema for updating a category
class CategoryUpdate(CategoryBase):
    new_name: Optional[str]

# Schema for reading a category
class CategoryRead(CategoryBase):
    category_id: int
    created_at: datetime
    updated_at: Optional[datetime]
