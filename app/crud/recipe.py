from typing import List, Optional
from sqlmodel import Session, select
from datetime import datetime

from app.models.recipe import Recipe
from app.schemas.recipe import RecipeCreate, RecipeUpdate

def create_recipe(db: Session, recipe_create: RecipeCreate, user_id: int) -> Recipe:
    """Create a new recipe."""
    recipe = Recipe(
        **recipe_create.model_dump(),
        user_id=user_id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe

def get_recipe(db: Session, recipe_id: int) -> Optional[Recipe]:
    """Retrieve a recipe by its ID."""
    statement = select(Recipe).where(Recipe.recipe_id == recipe_id)
    return db.exec(statement).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 10) -> List[Recipe]:
    """Retrieve multiple recipes with pagination."""
    statement = select(Recipe).offset(skip).limit(limit)
    return db.exec(statement).all()

def update_recipe(db: Session, recipe_id: int, recipe_update: RecipeUpdate) -> Optional[Recipe]:
    """Update an existing recipe."""
    recipe = get_recipe(db, recipe_id)
    if not recipe:
        return None
    recipe_data = recipe_update.model_dump(exclude_unset=True)
    for key, value in recipe_data.items():
        setattr(recipe, key, value)
    recipe.updated_at = datetime.now()
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe

def delete_recipe(db: Session, recipe_id: int) -> bool:
    """Delete a recipe."""
    recipe = get_recipe(db, recipe_id)
    if not recipe:
        return False
    db.delete(recipe)
    db.commit()
    return True

def get_recipes_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 10) -> List[Recipe]:
    """Retrieve recipes created by a specific user."""
    statement = select(Recipe).where(Recipe.user_id == user_id).offset(skip).limit(limit)
    return db.exec(statement).all()
