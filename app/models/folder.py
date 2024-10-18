
from typing import Optional, List
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship

class Folder(SQLModel, table=True):
    """SQLModel for the folders table."""
    __tablename__ = "folders"

    folder_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id")
    name: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)    
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)    

    # Relationships
    user: Optional["User"] = Relationship(back_populates="folders")
    recipes: List["FolderRecipe"] = Relationship(back_populates="folder")
