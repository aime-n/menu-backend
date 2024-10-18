# from __future__ import annotations
# from typing import Optional, TYPE_CHECKING
# from datetime import datetime, timezone
# from sqlmodel import Field, SQLModel, Relationship
# from sqlalchemy.orm import Mapped, relationship

# if TYPE_CHECKING:
#     from .user import User
#     from .recipe import Recipe

    
# class Like(SQLModel, table=True):
#     """SQLModel for the likes table."""
#     __tablename__ = "likes"
#     __table_args__ = {"schema": "recipes_db"}

#     like_id: Optional[int] = Field(default=None, primary_key=True)
#     user_id: int = Field(foreign_key="recipes_db.users.user_id")
#     recipe_id: int = Field(foreign_key="recipes_db.recipes.recipe_id")
#     created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))

#     # Relationships
#     user: Mapped[Optional["User"]] = relationship(back_populates="likes")
#     recipe: Mapped[Optional["Recipe"]] = relationship(back_populates="likes")
