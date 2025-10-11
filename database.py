# database.py
import sqlite3
import hashlib

def init_db():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Cơ sở dữ liệu đã được khởi tạo thành công.")

if __name__ == "__main__":
    init_db()