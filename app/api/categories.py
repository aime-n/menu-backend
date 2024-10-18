from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.models import Category
from typing import List
from app.schemas.category import CategoryCreate, CategoryRead, CategoryUpdate
from app.crud.category import create_category, read_category, update_category, read_categories

router = APIRouter()

@router.get("/", response_model=List[Category])
def get_all_categories(session: Session = Depends(get_session)):
    """
    Retrieve all categories.
    """
    return read_categories(session)


@router.post("/", response_model=CategoryRead)
def create_new_category(category: CategoryCreate, session: Session = Depends(get_session)):
    """Create a new category."""
    return create_category(session, category)

@router.get("/{category_id}", response_model=CategoryRead)
def get_category(category_id: int, session: Session = Depends(get_session)):
    """Retrieve a category by its ID."""
    return read_category(session, category_id)

@router.patch("/{category_id}", response_model=CategoryRead)
def update_existing_category(category_id: int, category: CategoryUpdate, session: Session = Depends(get_session)):
    """Update a category."""
    return update_category(session, category_id, category)
