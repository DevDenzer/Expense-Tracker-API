from fastapi import FastAPI
from app.routes import expenses
from app.database import create_table
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(expenses.router)