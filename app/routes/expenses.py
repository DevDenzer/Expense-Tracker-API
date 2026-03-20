from fastapi import APIRouter
from app.database import *

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Expense Tracker API is running!"}

@router.get("/expenses")
def read_expenses():
    expenses = get_all_expenses()

    result = []

    for exp_id, category, amount in expenses:
        result.append({
            "id": exp_id,
            "category": category,
            "amount": amount
        })

    return result

@router.post("/expenses")
def create_expense(category: str, amount: float):

    insert_expense(category, amount)

    return {
        "message": "Expense added successfully",
        "category": category,
        "amount": amount
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