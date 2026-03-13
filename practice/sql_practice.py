import sqlite3

# Connect to/create database file
conn = sqlite3.connect("expenses.db")

# Creating a cursor
cursor = conn.cursor()

# Creating table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTERGER PRIMARY KEY,
    category TEXT,
    ammount REAL
)
""")

# Inserting sample data
cursor.execute("INSERT INTO expenses (category, ammount) VALUES (?, ?)", ("Rent", 900))
cursor.execute("INSERT INTO expenses (category, ammount) VALUES (?, ?)", ("Food", 300))
cursor.execute("INSERT INTO expenses (category, ammount) VALUES (?, ?)", ("Utilities", 150))

# Saving changes
conn.commit()

# Query data
cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()

print("All Expenses:")
for row in rows:
    print(row)

conn.close()