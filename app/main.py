from fastapi import FastAPI
from app.routes import expenses
from app.database import create_table

app = FastAPI()

@app.on_event("startup")
def startup():
    create_table()

app.include_router(expenses.router)