# db/helpers.py
import sqlite3
from typing import Optional, Dict

DB_FILE = "secure_messages.db"

def create_user(username: str, password_hash: str, encryption_key: str) -> int:
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, password_hash, encryption_key) VALUES (?, ?, ?)",
        (username, password_hash, encryption_key)
    )
    conn.commit()
    user_id = cur.lastrowid
    conn.close()
    return user_id

def get_user_by_username(username: str) -> Optional[Dict]:
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, username, password_hash, encryption_key FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "username": row[1], "password_hash": row[2], "encryption_key": row[3]}
    return None
