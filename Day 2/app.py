from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


app= FastAPI()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

books= [
    {
        "id":1,
        "title": "Allen B. Doweny",
        "publisher": "O'Reilly",
        "published_date": "2021-10-07",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id":2,
        "title": "Django By Jerry",
        "publisher": "Jerry",
        "published_date": "2022-11-17",
        "page_count": 2134,
        "language": "Italian",
    },
    {
        "id":3,
        "title": "The Web Socket Handbook",
        "publisher": "Jeffery",
        "published_date": "2022-09-07",
        "page_count": 1034,
        "language": "Spanish",
    },
    {
        "id":4,
        "title": "Head First Javascript",
        "publisher": "Ismail",
        "published_date": "2021-04-17",
        "page_count": 1740,
        "language": "English",
    },
    
] 

class Book(BaseModel):
    id : int
    title : str
    publisher: str
    published_date: str
    page_count: int
    language: str
    


#return all books
@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books


#getting a specific book
@app.get('/book/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Book not found"
        )
    

#delete
@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return  # No content to return
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Book not found"
    )







