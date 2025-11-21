# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a complete REST API using FastAPI framework to practice modern web development, HTTP methods, data validation, and API design principles.

## 📝 Tasks

### 🛠️ Books Management API

#### Description
Create a RESTful API for managing a collection of books. The API should support all CRUD operations (Create, Read, Update, Delete) and include proper data validation, error handling, and documentation.

#### Requirements
Completed program should:

- Create a FastAPI application with proper project structure
- Define a Book model with fields: id, title, author, publication_year, genre, and is_available
- Implement GET /books endpoint to retrieve all books with optional filtering by genre
- Implement GET /books/{book_id} endpoint to retrieve a specific book by ID
- Implement POST /books endpoint to add new books with data validation
- Implement PUT /books/{book_id} endpoint to update existing books
- Implement DELETE /books/{book_id} endpoint to remove books
- Include proper HTTP status codes (200, 201, 404, 422) for different scenarios
- Add input validation using Pydantic models
- Generate automatic API documentation accessible via /docs
- Handle edge cases like book not found and invalid data


### 🛠️ Advanced Features

#### Description
Enhance the basic API with additional features to demonstrate advanced FastAPI concepts and best practices.

#### Requirements
Completed program should:

- Add query parameters for pagination (limit, offset) on the GET /books endpoint
- Implement search functionality with a GET /books/search?query= endpoint
- Add a GET /books/stats endpoint that returns statistics (total books, books by genre)
- Include response models to control API output format
- Add proper error handling with custom exception handlers
- Implement basic logging for API requests and errors
- Include dependency injection for database connection simulation
- Add middleware for CORS support
- Create comprehensive test cases for at least 3 endpoints