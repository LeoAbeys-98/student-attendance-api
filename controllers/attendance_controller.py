from flask import request, jsonify
from models.db import mysql
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from middleware.auth_middleware import role_required

@role_required('teacher')
@jwt_required() 
def mark_attendance():
    data = request.get_json()

    student_id = data['student_id']
    status = data['status']  # present / absent

    today = date.today()

    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)",
            (student_id, today, status)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({"message": "Attendance marked"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@jwt_required()
def get_attendance():

    student_id = request.args.get('student_id')
    date = request.args.get('date')

    try:
        cur = mysql.connection.cursor()

        query = """
            SELECT students.name, attendance.date, attendance.status
            FROM attendance
            JOIN students ON students.id = attendance.student_id
            WHERE 1=1
        """

        values = []

        # Filter by student
        if student_id:
            query += " AND attendance.student_id = %s"
            values.append(student_id)

        # Filter by date
        if date:
            query += " AND attendance.date = %s"
            values.append(date)

        cur.execute(query, tuple(values))

        data = cur.fetchall()

        cur.close()

        results = []

        for row in data:
            results.append({
                "student_name": row[0],
                "date": str(row[1]),
                "status": row[2]
            })

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
