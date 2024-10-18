
from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship

    
class Like(SQLModel, table=True):
    """SQLModel for the likes table."""
    __tablename__ = "likes"

    like_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id")
    recipe_id: int = Field(foreign_key="recipes.recipe_id")
    created_at: datetime = Field(default_factory=datetime.now)
    
    # Relationships
    user: Optional["User"] = Relationship(back_populates="likes")
    recipe: Optional["Recipe"] = Relationship(back_populates="likes")
