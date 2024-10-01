from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid

class Book(SQLModel, table=True):
    __tablename__ = "books"
    
    uid : uuid.UUID = Field(
        sa_column= Column(
            pg.UUID(as_uuid=True),
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
            
        )
    )
    title: str = Field(
        Column(
           pg.TEXT,
           nullable=False, 
        
        )
    )
    publisher: str = Field(
        Column(
            pg.TEXT,
            nullable=False
        )
    )
    published_date: str= Field(
        Column(
            pg.DATE,
            nullable=False
        )
    )
    page_count: int = Field(
        Column(
            pg.INTEGER,
            nullable=False
            
        )
    )
    language: str= Field(
        Column(
            pg.TEXT,
            nullable=False
        )
    )
    created_at: datetime = Field (
        Column(
            pg.TIMESTAMP,
            nullable=False,
            default=datetime.now
        )
    )
    updated_at: datetime = Field (
        Column(
            pg.TIMESTAMP,
            nullable=False,
            default=datetime.now
        )
    )
    
    def __repr__(self):
        return f"<Book> {self.title}>"
    
