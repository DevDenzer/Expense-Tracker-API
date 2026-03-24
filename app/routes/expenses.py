from fastapi import APIRouter
from app.database import *
from typing import List
from app.models import Expense, ExpenseResponse

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Expense Tracker API is running!"}

@router.get("/expenses", response_model=List[ExpenseResponse])
def read_expenses():
    return get_all_expenses()


@router.post("/expenses")
def create_expense(expense: Expense):

    insert_expense(expense.category, expense.amount)

    return {
        "message": "Expense added successfully",
        "category": expense.category,
        "amount": expense.amount
    }

@router.delete("/expenses/{expense_id}")
def delete_expense_endpoint(expense_id: int):

    delete_expense(expense_id)

    return {
        "message": f"Expense {expense_id} deleted successfully"
    }

@router.put("/expenses/{expense_id}")
def update_expense_endpoint(expense_id: int, category: str, amount: float):

    update_expense(expense_id, category, amount)

    return {
        "message": "Expense updated successfully",
        "id": expense_id,
        "category": category,
        "amount": amount
    }