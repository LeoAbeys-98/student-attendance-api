📌 Student Attendance Management System (Flask + MySQL + JWT)
📖 Project Overview
This project is a backend REST API system built using Flask and MySQL for managing student attendance efficiently. It supports user authentication, student management, attendance marking, and reporting features.
The system is designed with a modular architecture following real-world backend development practices.


🚀 Features
👤 User Registration (Admin / Teacher / Student)
🔐 Secure Login with JWT Authentication
🎓 Add and manage students
📅 Mark daily attendance (Present / Absent)
📊 View attendance reports
🔗 MySQL database integration
🧱 Modular project structure (routes, controllers, models)


🛠️ Tech Stack
Python
Flask
MySQL (XAMPP)
Flask-MySQLdb
Flask-JWT-Extended
bcrypt (Password hashing)


📁 Project Structure
attendance_api/
│
├── app.py
├── config.py
├── .env
│
├── routes/
│   ├── auth_routes.py
│   ├── student_routes.py
│   └── attendance_routes.py
│
├── controllers/
│   ├── auth_controller.py
│   ├── student_controller.py
│   └── attendance_controller.py
│
└── models/
    └── db.py


⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/student-attendance-api.git
cd student-attendance-api
2️⃣ Create virtual environment
python -m venv venv
Activate:
Mac/Linux
source venv/bin/activate
Windows
venv\Scripts\activate
3️⃣ Install dependencies
pip install flask flask-mysqldb flask-jwt-extended python-dotenv bcrypt
4️⃣ Setup MySQL (XAMPP)
Create database:
CREATE DATABASE attendance_system;
Create tables:
users
students
attendance
5️⃣ Configure environment variables
Create .env file:
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DB=attendance_system
JWT_SECRET_KEY=your_secret_key
6️⃣ Run the project
python app.py
Server runs at:
http://127.0.0.1:5000/


📌 API Endpoints

🔐 Authentication
POST /auth/register → Register user
POST /auth/login → Login user (returns JWT token)
🎓 Students
POST /student/add → Add student

📅 Attendance
POST /attendance/mark → Mark attendance
GET /attendance/report → View attendance report

🧪 Sample Login Request
{
  "email": "test@gmail.com",
  "password": "123456"
}


📊 Future Improvements
Frontend dashboard (React / HTML)
Role-based access control
Attendance filtering by date
Deployment on cloud (Render / Railway)
Email notifications


👨‍💻 Author
Bhathiya Abeysinghe
Computer Science Graduate
📍 Germany
