import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "expenses.db")

conn = sqlite3.connect(DB_PATH)

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            amount REAL NOT NULL
        )
        """)

    conn.commit()
    conn.close()

def insert_expense(category, amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (category, amount) VALUES (?, ?)",
        (category, amount)
    )

    conn.commit()
    conn.close()

def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

def get_total_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0

def get_all_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, category, amount FROM expenses")
    rows = cursor.fetchall()

    conn.close()

    return rows

def update_expense(expense_id, new_category, new_amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE expenses SET category = ?, amount = ? WHERE id = ?",
        (new_category, new_amount, expense_id)
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Table successfully created")