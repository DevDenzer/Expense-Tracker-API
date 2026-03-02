import sqlite3

def get_connection():
    return sqlite3.connect("expenses.db")

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

    cursor.execute("SELECT category, amount FROM expenses")
    rows = cursor.fetchall()

    conn.close()

    return rows

if __name__ == "__main__":
    create_table()
    print("Table successfully created")