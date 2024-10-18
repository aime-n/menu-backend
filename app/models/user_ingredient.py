# from __future__ import annotations
# from typing import Optional, TYPE_CHECKING
# from datetime import datetime, timezone
# from sqlmodel import Field, SQLModel, Relationship
# 

# if TYPE_CHECKING:
#     from .user import User
#     from .ingredient import Ingredient

    
# class UserIngredient(SQLModel, table=True):
#     """SQLModel for the user_ingredients table."""
#     __tablename__ = "user_ingredients"
#     __table_args__ = {"schema": "recipes_db"}

#     user_id: int = Field(foreign_key="recipes_db.users.user_id", primary_key=True)
#     ingredient_id: int = Field(foreign_key="recipes_db.ingredients.ingredient_id", primary_key=True)
#     added_date: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
#     updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))

#     # Relationships
#     user: Optional["User"]] = Relationship(back_populates="ingredients")
#     ingredient: Optional["Ingredient"]] = Relationship(back_populates="user_associations")
