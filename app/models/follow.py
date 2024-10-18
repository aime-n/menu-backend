# from __future__ import annotations
# from typing import Optional, TYPE_CHECKING
# from datetime import datetime, timezone
# from sqlmodel import Field, SQLModel, Relationship
# 

# if TYPE_CHECKING:
#     from .user import User


# class Follow(SQLModel, table=True):
#     """SQLModel for the follows table."""
#     __tablename__ = "follows"
#     __table_args__ = {"schema": "recipes_db"}

#     follower_id: int = Field(foreign_key="recipes_db.users.user_id", primary_key=True)
#     followed_id: int = Field(foreign_key="recipes_db.users.user_id", primary_key=True)
#     created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))

#     # Relationships
#     follower: Optional["User"]] = Relationship(back_populates="following", sa_relationship_kwargs={"primaryjoin": "User.user_id==Follow.follower_id"})
#     followed: Optional["User"]] = Relationship(back_populates="followers", sa_relationship_kwargs={"primaryjoin": "User.user_id==Follow.followed_id"})
