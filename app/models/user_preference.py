
from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship


class UserPreference(SQLModel, table=True):
    """SQLModel for the user_preferences table."""
    __tablename__ = "user_preferences"
    

    preference_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id")
    preference_type: str = Field(max_length=50)
    value: str = Field(max_length=100)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)

    # Relationships
    user: Optional["User"] = Relationship(back_populates="preferences")
