import sqlite3


def create_db():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT,
        result TEXT,
        secret_key TEXT,
        action TEXT,
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def insert_message(message, result, key, action):
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO messages(message, result, secret_key, action)
    VALUES(?,?,?,?)
    """, (message, result, key, action))

    conn.commit()
    conn.close()


def get_messages():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")

    rows = cursor.fetchall()

    conn.close()

    return rows