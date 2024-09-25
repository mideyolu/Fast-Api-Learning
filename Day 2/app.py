from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


#creating the app
app= FastAPI()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

#book list dictionary 
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

class BookUpdateModel(BaseModel):
    title : str
    publisher: str
    page_count: int
    language: str
    


#create
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    # Check if the book with the same ID already exists
    for existing_book in books:
        if existing_book["id"] == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    
    # Append the new book to the list using model_dump
    books.append(book.model_dump())
    return book

        

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
    
#update
@app.patch('/book/{book_id}')
async def update_book(book_id: int, book_data: BookUpdateModel):
    # Search for the book by id
    for book in books:
        if book['id'] == book_id:
            # Only update fields that are provided (i.e., not None)
            if book_data.title is not None:
                book['title'] = book_data.title
            if book_data.publisher is not None:
                book['publisher'] = book_data.publisher
            if book_data.page_count is not None:
                book['page_count'] = book_data.page_count
            if book_data.language is not None:
                book['language'] = book_data.language
            
            # Return the updated book
            return book
    
    # If no book with the provided id is found, raise an error
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







