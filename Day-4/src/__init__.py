from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting.....................")
    await init_db()
    yield
    print(f"Server has been stopped ............................")

#creating a version
version= "v1"

app= FastAPI(
    title= "Bookly",
    description="RESTAPI for a book review web service",
    version=version,
    lifespan=life_span
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