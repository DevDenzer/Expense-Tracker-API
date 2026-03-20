from pydantic import BaseModel

class Expense(BaseModel):
    category: str
    amount: float

    
if __name__ == "__main__":
    test_expense = Expense("Rent", 900)
    print(test_expense.display())