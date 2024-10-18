# from __future__ import annotations
# from typing import Optional, List, TYPE_CHECKING
# from datetime import datetime, timezone
# from sqlmodel import Field, SQLModel, Relationship
# 

# if TYPE_CHECKING:
#     from .recipe import Recipe
#     from .user import User

# class Comment(SQLModel, table=True):
#     """SQLModel for the comments table."""
#     __tablename__ = "comments"
#     __table_args__ = {"schema": "recipes_db"}

#     comment_id: Optional[int] = Field(default=None, primary_key=True)
#     recipe_id: int = Field(foreign_key="recipes_db.recipes.recipe_id")
#     user_id: int = Field(foreign_key="recipes_db.users.user_id")
#     parent_comment_id: Optional[int] = Field(foreign_key="recipes_db.comments.comment_id")
#     content: str
#     created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
#     updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))

#     # Relationships
#     recipe: Optional["Recipe"]] = Relationship(back_populates="comments")
#     user: Optional["User"]] = Relationship(back_populates="comments")
#     parent_comment: Optional[Comment]] = relationship(
#         sa_relationship_kwargs={"remote_side": "Comment.comment_id"},
#         back_populates="replies"
#     )
#     replies: List[Comment]] = Relationship(back_populates="parent_comment")

#     # recipe: Optional["Recipe"] = Relationship(back_populates="comments")
#     # user: Optional["User"] = Relationship(back_populates="comments")
#     # parent_comment: Optional[Comment] = relationship(
#     #     sa_relationship_kwargs={"remote_side": "Comment.comment_id"},
#     #     back_populates="replies"
#     # )
#     # replies: List[Comment] = Relationship(back_populates="parent_comment")
