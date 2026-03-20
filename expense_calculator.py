from app.models import Expense
from app.database import create_table, insert_expense, get_total_expenses, get_all_expenses, delete_expense, update_expense
print("Program started")

def get_float_input(prompt):
        while True:
            try:
                value = float(input(prompt))

                if value < 0:
                    print("Please enter a positive number...")
                    continue

                return value
            
            except ValueError:
                print("Please enter a valid number...")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number...")

def add_expense():
    while True:
        category = input("Enter expense category (or type 'done' to finish): ")

        if category.lower() == "done":
            break

        amount = get_float_input(f"Enter amount for {category}: ")
        insert_expense(category, amount)
        print("Expense added.\n")

def view_all_expenses():
    print("\n=== All Expenses ===")

    expenses = get_all_expenses()

    if not expenses:
        print("No expenses found.")
        return
    
    for exp_id, category, amount in expenses:
        print(f"[{exp_id}] {category}: ${amount:.2f}")

def delete_expense_cli():
    view_all_expenses()

    try:
        expense_id = get_int_input("Enter the ID of the expense to delete: ")
        delete_expense(expense_id)
        print("Expense deleted.\n")
    except ValueError:
        print("Invalid ID. Please retry.")

def view_total_expenses():
    total = get_total_expenses()
    print(f"\nTotal expenses: ${total:.2f}")

def update_expense_cli():
    view_all_expenses()

    try:
        expense_id = get_int_input("Enter the ID of the expense you would like to update: ")
        new_category = input("Enter the new category: ")
        new_amount = get_float_input("Enter the new amount: ")

        update_expense(expense_id, new_category, new_amount)

        print("Expense updated.\n")

    except ValueError:
        print("Invalid input. Please retry.")

def main():
    create_table()

    print("=== Monthly Expense Calculator ===")

    income = get_float_input("Enter your monthly income:  ")
        
    while True:
        print("\n== Expense Tracker Menu ==")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Remaining Balance")
        print("4. Delete Expense")
        print("5. Update Expense")
        print("6. Exit")

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
            delete_expense_cli()

        elif choice == "5":
            update_expense_cli()

        elif choice == "6":
            print("\n=== Summary (from Database) ===")

            all_expenses = get_all_expenses()

            total = get_total_expenses()
            remaining = income - total
            
            print(f"Monthly Income: ${income:.2f}")

            for _, category, amount in all_expenses:
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