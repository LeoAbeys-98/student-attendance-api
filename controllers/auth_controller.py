from flask import request, jsonify
from models.db import mysql
import bcrypt
from flask_jwt_extended import create_access_token
import bcrypt
from flask import request, jsonify
from models.db import mysql

def register():
    data = request.get_json()

    name = data['name']
    email = data['email']
    password = data['password']
    role = data.get('role', 'student')

    # 🔐 Hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cur = mysql.connection.cursor()

        cur.execute(
            "INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
            (name, email, hashed_password, role)
        )

        mysql.connection.commit()
        cur.close()

        return jsonify({"message": "User registered successfully"}), 201
    
    

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def login():
    data = request.get_json()

    email = data['email']
    password = data['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, email, password, role FROM users WHERE email=%s", (email,))
    user = cur.fetchone()
    cur.close()

    if not user:
        return jsonify({"message": "User not found"}), 404

    stored_password = user[3]

    # check password
    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        token = create_access_token(identity={"id": user[0], "role": user[4]})

        return jsonify({
            "message": "Login successful",
            "token": token
        }), 200

    return jsonify({"message": "Invalid credentials"}), 401
    
    