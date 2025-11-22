import sqlite3
from datetime import datetime

DB_FILE = "secure_messages.db"  # This will be in your project root

def create_tables():
    """Create messages table if it doesn't exist"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encrypted_message TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_message(encrypted_message: str):
    """Save an encrypted message to the database"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO messages (encrypted_message, created_at)
        VALUES (?, ?)
    """, (encrypted_message, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def get_messages():
    """Retrieve all messages"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, encrypted_message, created_at FROM messages")
    rows = cursor.fetchall()
    conn.close()
    return rows
