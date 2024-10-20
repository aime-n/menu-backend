# api/recipes.py

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.schemas.recipe import RecipeCreate, RecipeRead, RecipeUpdate
from app.crud.recipe import (
    create_recipe,
    get_recipe,
    get_recipes,
    update_recipe,
    delete_recipe,
    get_recipes_by_user
)
from app.database import get_session
from app.utils.auth import get_current_user
from app.models.user import User
from app.models.recipe import Recipe

router = APIRouter()

@router.post("/", response_model=RecipeRead, status_code=status.HTTP_201_CREATED)
def create_new_recipe(
    recipe_create: RecipeCreate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Create a new recipe."""
    recipe = create_recipe(db, recipe_create, user_id=current_user.user_id)
    return recipe

@router.get("/{recipe_id}", response_model=RecipeRead)
def read_recipe(recipe_id: int, db: Session = Depends(get_session)):
    """Retrieve a recipe by its ID."""
    recipe = get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.get("/", response_model=List[RecipeRead])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    """Retrieve multiple recipes with pagination."""
    recipes = get_recipes(db, skip=skip, limit=limit)
    return recipes

@router.get("/user/{user_id}", response_model=List[RecipeRead])
def read_user_recipes(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    """Retrieve recipes created by a specific user."""
    recipes = get_recipes_by_user(db, user_id=user_id, skip=skip, limit=limit)
    return recipes

@router.put("/{recipe_id}", response_model=RecipeRead)
def update_existing_recipe(
    recipe_id: int,
    recipe_update: RecipeUpdate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Update an existing recipe."""
    recipe = get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    if recipe.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this recipe")
    updated_recipe = update_recipe(db, recipe_id, recipe_update)
    return updated_recipe

@router.delete("/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_recipe(
    recipe_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Delete a recipe."""
    recipe = get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    if recipe.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this recipe")
    success = delete_recipe(db, recipe_id)
    if not success:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return None
