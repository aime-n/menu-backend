from typing import List, Optional
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel


class Category(SQLModel, table=True):
    __tablename__ = "categories"
    category_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    parent_id: Optional[int] = Field(default=None, foreign_key="categories.category_id")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default=None, nullable=True)  


    # Relationships
    parent: Optional["Category"] = Relationship(
        back_populates="children",
        sa_relationship_kwargs={"remote_side": "Category.category_id"}
    )
    children: List["Category"] = Relationship(back_populates="parent")
    ingredients: List["Ingredient"] = Relationship(back_populates="category")
