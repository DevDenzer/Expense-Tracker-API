# Expense Tracker API

This Python backend project began as a CLI expense calculator and later expanded into a REST API using FastAPI

This application allows users to create, view, update, and delete expenses while storing data in a SQLite database

## Features
- CLI-based monthly expense calculator
- Handles income and multiple expense categories
- Calculates remaining balance
- Full CRUD operations
- SQLite database integration
- FastAPI REST API
- Interactive API documentation

## Tech Stack
- Python
- SQLite
- FastAPI
- Uvicorn
- Git/Github

## API Endpoints
GET /expenses
POST /expenses
PUT /expenses/{id}
DELETE /expenses/{id}

## Running the Project

- install dependencies:
    pip install fastapi uvicorn

- Run the API server:
    python -m uvicorn api:app --reload

- Open the interactive API docs
    https://127.0.0.1:800/docs

### Project Files
api.py - FastAPI backend
database.py - Database connection and queries
expense_calculator.py - CLI expense calculator

#### Development Goals
- Strengthen Python fundamentals
- Practice Git workflow
- Learn database interaction with SQLite
- Build small complete backend tools