from flask import request, jsonify
from models.db import mysql
from flask_jwt_extended import jwt_required, get_jwt_identity   
from middleware.auth_middleware import role_required

@role_required('admin')
@jwt_required() 
def add_student():
    current_user = get_jwt_identity()
    data = request.get_json()
    

    name = data['name']
    email = data['email']
    course = data['course']

    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)",
            (name, email, course)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({"message": "Student added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500