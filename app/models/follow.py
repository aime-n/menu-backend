
from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship


class Follow(SQLModel, table=True):
    """SQLModel for the follows table."""
    __tablename__ = "follows"

    follower_id: int = Field(foreign_key="users.user_id", primary_key=True)
    followed_id: int = Field(foreign_key="users.user_id", primary_key=True)
    created_at: Optional[datetime] = Field(default=None, nullable=True)  

    # Relationships
    follower: Optional["User"] = Relationship(back_populates="following", sa_relationship_kwargs={"primaryjoin": "User.user_id==Follow.follower_id"})
    followed: Optional["User"] = Relationship(back_populates="followers", sa_relationship_kwargs={"primaryjoin": "User.user_id==Follow.followed_id"})
