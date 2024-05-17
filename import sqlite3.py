import sqlite3

# Connect to SQLite database (create if not exists)
conn = sqlite3.connect('login.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define a SQL statement to create a table
create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
"""

# Execute the SQL statement to create the table
cursor.execute(create_table_sql)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()