from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE users (username text, password text, role text)''')
    c.execute("INSERT INTO users VALUES ('admin', 'super_secret_123', 'admin')")
    conn.commit()
    return conn

db_conn = init_db()

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', '')
    password = data.get('password', '')
    
    cursor = db_conn.cursor()
    # Vulnerability: Classic String Concatenation SQLi
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return jsonify({"status": "success", "role": user[2]})
        return jsonify({"status": "failed", "message": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080)