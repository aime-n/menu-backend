from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class Follow(SQLModel, table=True):
    """SQLModel for the follows table."""
    __tablename__ = "follows"

    follower_id: int = Field(
        foreign_key="users.user_id",
        primary_key=True
    )
    followed_id: int = Field(
        foreign_key="users.user_id",
        primary_key=True
    )
    created_at: Optional[datetime] = Field(default=None, nullable=True)

    # Relationships
    follower: Optional["User"] = Relationship(
        back_populates="following",
        sa_relationship_kwargs={
            "primaryjoin": "Follow.follower_id == User.user_id"
        }
    )
    followed: Optional["User"] = Relationship(
        back_populates="followers",
        sa_relationship_kwargs={
            "primaryjoin": "Follow.followed_id == User.user_id"
        }
    )
