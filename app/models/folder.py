# from __future__ import annotations
# from typing import Optional, List, TYPE_CHECKING
# from datetime import datetime, timezone
# from sqlmodel import Field, SQLModel, Relationship
# from sqlalchemy.orm import Mapped, relationship

# if TYPE_CHECKING:
#     from .user import User
#     from .folder_recipe import FolderRecipe

# class Folder(SQLModel, table=True):
#     """SQLModel for the folders table."""
#     __tablename__ = "folders"
#     __table_args__ = {"schema": "recipes_db"}

#     folder_id: Optional[int] = Field(default=None, primary_key=True)
#     user_id: int = Field(foreign_key="recipes_db.users.user_id")
#     name: str
#     description: Optional[str] = None
#     created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
#     updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))

#     # Relationships
#     user: Mapped[Optional["User"]] = relationship(back_populates="folders")
#     recipes: Mapped[List["FolderRecipe"]] = relationship(back_populates="folder")
