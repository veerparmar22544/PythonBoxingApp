import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create the users table
conn.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')

# Create the practice_logs table
conn.execute('''CREATE TABLE IF NOT EXISTS practice_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    log_text TEXT,
                    log_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )''')

# Commit changes
conn.commit()

# Close connection
conn.close()
def get_user_id(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ?", (username,))
    user_id = c.fetchone()
    conn.close()
    return user_id[0] if user_id else None

def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

def add_practice_log(user_id, log_text):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO practice_logs (user_id, log_text) VALUES (?, ?)", (user_id, log_text))
    conn.commit()
    conn.close()

def get_practice_logs(user_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT log_text, log_timestamp FROM practice_logs WHERE user_id = ?", (user_id,))
    logs = c.fetchall()
    conn.close()
    return logs
