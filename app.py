from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
from routes.auth_routes import auth_bp
from flask_jwt_extended import JWTManager   
from routes.student_routes import student_bp
from routes.attendance_routes import attendance_bp

load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # you can later move to .env
jwt = JWTManager(app)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(student_bp, url_prefix='/student')
app.register_blueprint(attendance_bp, url_prefix='/attendance')

# 🔗 MySQL connection settings (from XAMPP)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'attendance_system'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

@app.route('/')
def home():
    return "Flask is running!"

@app.route('/test-db')
def test_db():
    cur = mysql.connection.cursor()
    cur.execute("SELECT 1")
    return "Database Connected Successfully!"


if __name__ == '__main__':
    app.run(debug=True)