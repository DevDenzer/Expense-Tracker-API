class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def display(self):
        return f"{self.category}: ${self.amount:.2f}"
    
if __name__ == "__main__":
    test_expense = Expense("Rent", 900)
    print(test_expense.display())