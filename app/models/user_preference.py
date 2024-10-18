# from __future__ import annotations
# from typing import Optional, TYPE_CHECKING
# from datetime import datetime, timezone
# from sqlmodel import Field, SQLModel, Relationship
# 

# if TYPE_CHECKING:
#     from .user import User

# class UserPreference(SQLModel, table=True):
#     """SQLModel for the user_preferences table."""
#     __tablename__ = "user_preferences"
#     __table_args__ = {"schema": "recipes_db"}

#     preference_id: Optional[int] = Field(default=None, primary_key=True)
#     user_id: int = Field(foreign_key="recipes_db.users.user_id")
#     preference_type: str = Field(max_length=50)
#     value: str = Field(max_length=100)
#     created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
#     updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))

#     # Relationships
#     user: Optional["User"]] = Relationship(back_populates="preferences")

#     # user: Optional["User"] = Relationship(back_populates="preferences")
