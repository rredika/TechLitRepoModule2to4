from flask import Flask, jsonify, redirect, request, render_template, url_for, flash
import sqlite3
app = Flask(__name__)
app.secret_key = "secret123"

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return jsonify({
        "status" : "API is running",
        "message": "Server is up and operational"
    })

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    data = {
        "code": 200,
        "status": "success",
        "message": "List of users",
        "records": len(rows),
        "rows": [],
    }
    for row in rows:
        data['rows'].append({
            "id" : row["id"],
            "nama" : row["nama"],
            "username" : row["username"],
            "password" : row["password"],
            "level" : row["level"]
        })

    return render_template('users/index.html', data=data)
  

@app.route('/users/create', methods=['GET'])
def create_user():
    return render_template('users/create.html')

@app.route('/users/insert', methods=['POST'])
def create_user_post():
    nama = request.form['nama']
    username = request.form['username']
    password = request.form['password']
    level = request.form['level']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO users (nama, username, password, level)
                    VALUES (?, ?, ?, ?)""",
                    (nama, username, password, level))

    conn.commit()
    conn.close()

    return redirect(url_for('get_users', ))


@app.route('/users/<int:user_id>/edit', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    data = {
        "code": 200,
        "status": "success",
        "message": "User edit form",
        "rows": 
            {
                "id" : row["id"],
                "nama" : row["nama"],
                "username" : row["username"],
                "password" : row["password"],
                "level" : row["level"]
            },
    }

    return render_template('users/edit.html', data=data)
    return jsonify(data)  

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):

    nama = request.form['nama']
    username = request.form['username']
    password = request.form['password']
    level = request.form['level']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET nama=?, username=?, password=?, level=?
        WHERE id=?
    """, (nama, username, password, level, user_id))

    conn.commit()
    conn.close()

    flash('User updated successfully', 'success')
    return redirect(url_for('get_users', ))


@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    flash('User deleted successfully', 'success')
    return redirect(url_for('get_users', ))

if __name__ == '__main__':
    app.run(debug=True)