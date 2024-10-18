from typing import List, Optional
from sqlmodel import Session, select
from app.models import Ingredient
from app.schemas.ingredient import IngredientCreate, IngredientUpdate

def create_ingredient(db: Session, ingredient_data: IngredientCreate) -> Ingredient:
    """Create a new ingredient."""
    ingredient = Ingredient.model_validate(ingredient_data)
    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)
    return ingredient

def get_ingredient(db: Session, ingredient_id: int) -> Optional[Ingredient]:
    """Retrieve an ingredient by ID."""
    return db.get(Ingredient, ingredient_id)

def get_ingredients(db: Session, skip: int = 0, limit: int = 10) -> List[Ingredient]:
    """Retrieve a list of ingredients."""
    statement = select(Ingredient).offset(skip).limit(limit)
    return db.exec(statement).all()

def update_ingredient(db: Session, ingredient_id: int, ingredient_data: IngredientUpdate) -> Optional[Ingredient]:
    """Update an existing ingredient."""
    ingredient = get_ingredient(db, ingredient_id)
    if not ingredient:
        return None
    for key, value in ingredient_data.model_dump(exclude_unset=True).items():
        setattr(ingredient, key, value)
    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)
    return ingredient

def delete_ingredient(db: Session, ingredient_id: int) -> bool:
    """Delete an ingredient by ID."""
    ingredient = get_ingredient(db, ingredient_id)
    if not ingredient:
        return False
    db.delete(ingredient)
    db.commit()
    return True
