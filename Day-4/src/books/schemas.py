from pydantic import BaseModel

class Book(BaseModel):
    id : int
    title : str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title : str
    publisher: str
    page_count: int
    language: str