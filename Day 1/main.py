from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel


app= FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get('/')
async def home_route():
    return {"Message":"Hello World"}


@app.get('/greet')
async def greet_name(name: Optional[str] = "User", 
                     age: int=0) -> dict:
    return  {"Message":f"Hello {name}", "age": age}

#for query localhosturl/path?age=value
#for making optianl name query parameter import the optinal class and specify Optinal[dt]= 'val' the you use ?=name&age=value


#sending data to the server
#serialization model is used to validate data from clinet requests either from post request
class BookCreateModel(BaseModel):
    title : str
    author: str
    date: str 
    
    
@app.post('/create_book')
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author,
        "date": book_data.date
    }


@app.get('/get_headers', status_code=201)
async def get_headers(
    accept:str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)
    
):
    request = {}
    request_headers ={}
    
    request_headers['Accept']= accept
    request_headers['Content-Type']= content_type
    request_headers['User-Agent']= user_agent
    request_headers['Host']= host
    
    return request_headers

