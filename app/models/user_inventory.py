
from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship


    
class UserInventory(SQLModel, table=True):
    """SQLModel for the user_ingredients table."""
    __tablename__ = "user_inventory"

    user_id: int = Field(foreign_key="users.user_id", primary_key=True)
    ingredient_id: int = Field(foreign_key="ingredients.ingredient_id", primary_key=True)
    added_date: Optional[datetime] = Field(default=None, nullable=True)  
    updated_at: Optional[datetime] = Field(default=None, nullable=True)  

    # Relationships
    user: Optional["User"] = Relationship(back_populates="ingredients")
    ingredient: Optional["Ingredient"] = Relationship(back_populates="user_associations")
