# FastAPI REST API - Starter Code
# Students: Complete the TODOs below to build a complete Books Management API

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Books Management API",
    description="A REST API for managing a collection of books",
    version="1.0.0"
)

# TODO: Define the Book Pydantic model
class Book(BaseModel):
    """
    TODO: Complete the Book model with the following fields:
    - id: int
    - title: str
    - author: str
    - publication_year: int (should be between 1000 and current year)
    - genre: str
    - is_available: bool (default True)
    
    Use appropriate Pydantic Field validators for data validation.
    """
    pass

# TODO: Define request models for creating/updating books
class BookCreate(BaseModel):
    """Model for creating new books (without id)"""
    pass

class BookUpdate(BaseModel):
    """Model for updating books (all fields optional)"""
    pass

# In-memory database simulation
books_db: List[Book] = [
    # TODO: Add 3-5 sample books for testing
]

# TODO: Helper function to find book by ID
def find_book_by_id(book_id: int) -> Optional[Book]:
    """Find and return a book by its ID"""
    pass

# TODO: Helper function to generate new ID
def get_next_id() -> int:
    """Generate the next available ID"""
    pass

# API Endpoints

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to Books Management API", "docs": "/docs"}

# TODO: GET /books - Retrieve all books with optional filtering
@app.get("/books", response_model=List[Book])
def get_books(
    genre: Optional[str] = Query(None, description="Filter books by genre"),
    limit: int = Query(10, ge=1, le=100, description="Number of books to return"),
    offset: int = Query(0, ge=0, description="Number of books to skip")
):
    """
    Retrieve all books with optional filtering and pagination
    
    TODO: Implement this endpoint to:
    - Return all books if no genre filter
    - Filter by genre if provided
    - Apply pagination using limit and offset
    - Return appropriate status codes
    """
    pass

# TODO: GET /books/{book_id} - Retrieve specific book
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """
    Retrieve a specific book by ID
    
    TODO: Implement this endpoint to:
    - Find book by ID
    - Return 404 if book not found
    - Return the book if found
    """
    pass

# TODO: POST /books - Create new book
@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    """
    Create a new book
    
    TODO: Implement this endpoint to:
    - Generate new ID for the book
    - Add book to database
    - Return created book with 201 status
    - Handle validation errors
    """
    pass

# TODO: PUT /books/{book_id} - Update existing book
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate):
    """
    Update an existing book
    
    TODO: Implement this endpoint to:
    - Find book by ID
    - Return 404 if book not found
    - Update only provided fields
    - Return updated book
    """
    pass

# TODO: DELETE /books/{book_id} - Delete book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """
    Delete a book by ID
    
    TODO: Implement this endpoint to:
    - Find book by ID
    - Return 404 if book not found
    - Remove book from database
    - Return success message
    """
    pass

# TODO: GET /books/search - Search books
@app.get("/books/search", response_model=List[Book])
def search_books(query: str = Query(..., min_length=1, description="Search query")):
    """
    Search books by title or author
    
    TODO: Implement this endpoint to:
    - Search in title and author fields (case-insensitive)
    - Return matching books
    - Return empty list if no matches
    """
    pass

# TODO: GET /books/stats - Get statistics
@app.get("/books/stats")
def get_books_stats():
    """
    Get books statistics
    
    TODO: Implement this endpoint to return:
    - Total number of books
    - Number of available books
    - Books count by genre
    - Average publication year
    """
    pass

# TODO: Add error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Custom 404 error handler"""
    pass

if __name__ == "__main__":
    # Run the application
    uvicorn.run(app, host="0.0.0.0", port=8000)

# TODO: Installation instructions
"""
To run this project:

1. Install required packages:
   pip install fastapi uvicorn

2. Run the application:
   python starter-code.py
   
3. Access the API:
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

4. Test endpoints using the interactive documentation or curl:
   curl -X GET "http://localhost:8000/books"
"""