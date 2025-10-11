# auth_server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import hashlib

app = Flask(__name__)
CORS(app) # Rất quan trọng: Cho phép frontend giao tiếp với server này

# Hàm kết nối CSDL (Lấy từ actions.py của bạn)
def get_db_connection():
    conn = sqlite3.connect('user_data.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Hàm băm mật khẩu (Lấy từ actions.py của bạn)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# API endpoint cho việc đăng nhập
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'success': False, 'message': 'Tên đăng nhập và mật khẩu không được để trống.'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    password_hash = hash_password(password)
    cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, password_hash))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({'success': True, 'message': 'Đăng nhập thành công!'})
    else:
        return jsonify({'success': False, 'message': 'Tên đăng nhập hoặc mật khẩu không chính xác.'}), 401

# API endpoint cho việc đăng ký
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'success': False, 'message': 'Tên đăng nhập và mật khẩu không được để trống.'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return jsonify({'success': False, 'message': f"Tên đăng nhập '{username}' đã tồn tại."}), 409

    password_hash = hash_password(password)
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': 'Đăng ký thành công! Vui lòng đăng nhập.'})

if __name__ == '__main__':
    # Chạy server này trên một cổng khác để không xung đột với Rasa
    app.run(port=5004, debug=True)