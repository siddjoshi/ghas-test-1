import sqlite3

def get_user_by_id(user_id: int):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # CodeQL may flag this as potential SQL injection
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchone()
