import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create the users table if it doesn't already exist
conn.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')

# Create the practice_logs table if it doesn't already exist
conn.execute('''CREATE TABLE IF NOT EXISTS practice_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    log_text TEXT,
                    log_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )''')

# Create the calorie_logs table if it doesn't already exist
conn.execute('''CREATE TABLE IF NOT EXISTS calorie_logs (
                    user_id INTEGER PRIMARY KEY,
                    total_calories INTEGER DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )''')

# Commit the changes
conn.commit()

# Close the connection to the database
conn.close()

# Function to add a new user to the users table
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Function to verify if a user exists with the given username and password
def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

# Function to get the user ID based on the username
def get_user_id(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ?", (username,))
    user_id = c.fetchone()
    conn.close()
    return user_id[0] if user_id else None

# Function to add a practice log for a specific user
def add_practice_log(user_id, log_text):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO practice_logs (user_id, log_text) VALUES (?, ?)", (user_id, log_text))
    conn.commit()
    conn.close()

# Function to get all practice logs for a specific user
def get_practice_logs(user_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM practice_logs WHERE user_id = ?", (user_id,))
    logs = c.fetchall()
    conn.close()
    return logs

# Function to get the total calorie count for a specific user
def get_calorie_count(user_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT total_calories FROM calorie_logs WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

# Function to update the total calorie count for a specific user
def update_calorie_count(user_id, total_calories):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO calorie_logs (user_id, total_calories) VALUES (?, ?)", (user_id, total_calories))
    conn.commit()
    conn.close()
