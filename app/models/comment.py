from typing import Optional, List
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship


class Comment(SQLModel, table=True):
    """SQLModel for the comments table."""
    __tablename__ = "comments"

    comment_id: Optional[int] = Field(default=None, primary_key=True)
    recipe_id: int = Field(foreign_key="recipes.recipe_id")
    user_id: int = Field(foreign_key="users.user_id")
    parent_comment_id: Optional[int] = Field(foreign_key="comments.comment_id")
    content: str
    created_at: Optional[datetime] = Field(default=None, nullable=True)  
    updated_at: Optional[datetime] = Field(default=None, nullable=True)  

    # Relationships
    recipe: Optional["Recipe"] = Relationship(back_populates="comments")
    user: Optional["User"] = Relationship(back_populates="comments")
    parent_comment: Optional["Comment"] = Relationship(
        back_populates="replies",
        sa_relationship_kwargs={"remote_side": "Comment.comment_id"},
    )
    replies: List["Comment"] = Relationship(back_populates="parent_comment")
