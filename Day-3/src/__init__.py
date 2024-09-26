from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.books.routes import book_router

#creating a version
version= "v1"

app= FastAPI(
    title= "Bookly",
    description="RESTAPI for a book review web service",
    version=version
)


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

#API router
app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])