import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Create the todo table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
''')

def add_todo(task):
    # Insert a new todo into the database
    cursor.execute('INSERT INTO todos (task) VALUES (?)', (task,))
    conn.commit()

def get_todos():
    # Retrieve all todos from the database
    cursor.execute('SELECT * FROM todos')
    return cursor.fetchall()

def mark_todo_complete(todo_id):
    # Mark a todo as completed in the database
    cursor.execute('UPDATE todos SET completed = 1 WHERE id = ?', (todo_id,))
    conn.commit()

def delete_todo(todo_id):
    # Delete a todo from the database
    cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()

# Close the database connection when done
conn.close()