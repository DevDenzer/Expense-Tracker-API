from expense_model import Expense
from database import create_table, insert_expense, get_total_expenses, get_all_expenses
print("Program started")
def add_expense():
    while True:
        category = input("Enter expense category (or type 'done' to finish): ")

        if category.lower() == "done":
            break

        amount = get_float_input(f"Enter amount for {category}: ")
        insert_expense(category, amount)
        print("Expense added.\n")

def get_float_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number...")

def view_all_expenses():
    print("\n=== All Expenses ===")

    expenses = get_all_expenses()

    if not expenses:
        print("No expenses found.")
        return
    
    for category, amount in expenses:
        print(f"{category}: ${amount:.2f}")

def view_total_expenses():
    total = get_total_expenses()
    print(f"\nTotal expenses: ${total:.2f}")

def main():
    create_table()

    print("=== Monthly Expense Calculator ===")

    income = get_float_input("Enter your monthly income:  ")
        
    while True:
        print("\n== Expense Tracker Menu ==")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Remaining Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            total = get_total_expenses()
            remaining = income - total
            print(f"\nRemaining Balance: ${remaining:.2f}")
        elif choice == "4":
            print("\n=== Summary (from Database) ===")
            all_expenses = get_all_expenses()
            print(f"Monthly Income: ${income:.2f}")

            for category, amount in all_expenses:
                print(f"{category}: ${amount:.2f}")
            print(f"Remaining Balance: ${remaining:.2f}")
            if remaining < 0:
                    print("Warning: You are overspending.")
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

    

if __name__ == "__main__":
    main()