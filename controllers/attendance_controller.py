from flask import request, jsonify
from models.db import mysql
from datetime import date

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
    
def get_attendance():
    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT students.name, attendance.date, attendance.status
            FROM attendance
            JOIN students ON students.id = attendance.student_id
        """)
        data = cur.fetchall()
        cur.close()

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
