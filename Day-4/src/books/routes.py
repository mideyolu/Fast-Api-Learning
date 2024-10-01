from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel
from typing import List



#api router
book_router = APIRouter()


@book_router.post("/", response_model=Book)
def create_book(book: Book):
    # Check if the book with the same ID already exists
    for existing_book in books:
        if existing_book["id"] == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    
    # Append the new book to the list using model_dump
    books.append(book.model_dump())
    return book

        


#return all books
@book_router.get('/', response_model=List[Book])
async def get_all_books():
    return books #returning all the books


#getting a specific book
@book_router.get('/{book_id}')
async def get_book(book_id: int) -> dict:
    
    #looking for a specific book
    for book in books:
        if book['id'] == book_id:
            return book
        
    #raise exception
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Book not found"
        )
    
    
#update
@book_router.patch('/{book_id}')
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
@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            #deleting a book
            books.remove(book)
            return  # No content to return
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Book not found"
    )







