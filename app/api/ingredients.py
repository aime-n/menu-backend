from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.database import get_session
from app.schemas.ingredient import IngredientCreate, IngredientRead, IngredientUpdate
from app.crud.ingredient import create_ingredient, get_ingredient, get_ingredients, update_ingredient, delete_ingredient

router = APIRouter()

@router.post("/", response_model=IngredientRead, status_code=201)
def create_ingredient_endpoint(ingredient_data: IngredientCreate, db: Session = Depends(get_session)):
    """Create a new ingredient."""
    return create_ingredient(db, ingredient_data)

@router.get("/{ingredient_id}", response_model=IngredientRead)
def read_ingredient(ingredient_id: int, db: Session = Depends(get_session)):
    """Retrieve an ingredient by ID."""
    ingredient = get_ingredient(db, ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

@router.get("/", response_model=List[IngredientRead])
def read_ingredients(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    """Retrieve a list of ingredients with pagination."""
    return get_ingredients(db, skip=skip, limit=limit)

@router.put("/{ingredient_id}", response_model=IngredientRead)
def update_ingredient_endpoint(ingredient_id: int, ingredient_data: IngredientUpdate, db: Session = Depends(get_session)):
    """Update an existing ingredient."""
    updated_ingredient = update_ingredient(db, ingredient_id, ingredient_data)
    if not updated_ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return updated_ingredient

@router.delete("/{ingredient_id}", status_code=204)
def delete_ingredient_endpoint(ingredient_id: int, db: Session = Depends(get_session)):
    """Delete an ingredient by ID."""
    success = delete_ingredient(db, ingredient_id)
    if not success:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return None
