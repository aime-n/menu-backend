from sqlmodel import Session, select
from typing import List, Optional
from app.models import Category
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryBase, CategoryRead
from fastapi import HTTPException
from datetime import datetime


def create_category(session: Session, category_data: CategoryCreate) -> CategoryBase:
    """Create a new category."""
    category = Category(**category_data.model_dump())
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def read_category(session: Session, category_id: int) -> CategoryRead:
    """Retrieve a category by its ID."""
    category = session.get(Category, category_id)
    if not category:
        # Raise a 404 error if the category does not exist
        raise HTTPException(status_code=404, detail="Category not found")
    return category

def read_categories(session: Session, skip: int = 0, limit: int = 10) -> List[CategoryBase]:
    """Retrieve a list of categories with optional pagination."""
    # statement = select(Category).offset(skip).limit(limit)
    statement = select(Category)
    results = session.exec(statement)
    return results.all()

def update_category(session: Session, category_id: int, category_data: CategoryUpdate) -> Optional[CategoryBase]:
    """Update an existing category."""
    category = session.get(Category, category_id)
    if not category:
        return None
    # category.name = category_data.new_name
    if not category:
        return None
    # Update the fields that have been provided
    ingredient_data_dict = category_data.dict(exclude_unset=True)
    for key, value in ingredient_data_dict.items():
        setattr(category, key, value)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def delete_category(session: Session, category_id: int) -> bool:
    """Delete a category by its ID."""
    category = session.get(Category, category_id)
    if not category:
        return False
    session.delete(category)
    session.commit()
    return True
