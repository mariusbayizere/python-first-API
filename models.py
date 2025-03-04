from sqlmodel import SQLModel, Field
import sqlalchemy.dialects.mysql as pg
import uuid
from typing import Optional
from datetime import datetime

class Student(SQLModel, table=True):
    """
    Represents a student with various attributes.
    """
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        nullable=False,
    )
    first_name: str = Field(
        max_length=100,
        nullable=False
    )
    last_name: str = Field(
        max_length=100,
        nullable=False
    )
    email: str = Field(
        max_length=255,
        unique=True,
        nullable=False, 
        index=True
    )
    faculty: str = Field(max_length=100)
    department: str = Field(max_length=100)
    level: int = Field(ge=1, le=6)
    cgpa: float = Field(ge=0.0, le=4.0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)


def __str__(self):
    return f"{self.first_name} {self.last_name} {self.email} {self.faculty} {self.department} {self.level} {self.cgpa} {self.created_at} {self.updated_at}"

def __repr__(self):
    return f"{self.first_name} {self.last_name} {self.email} {self.faculty} {self.department} {self.level} {self.cgpa} {self.created_at} {self.updated_at}"