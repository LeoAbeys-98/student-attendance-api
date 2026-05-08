# 📌 Student Attendance Management System (Flask + MySQL + JWT)

## 📖 Overview

This project is a backend REST API built using Flask and MySQL for managing student attendance in an academic environment. It includes authentication, role-based access control, and advanced attendance reporting features.

The system follows a modular architecture suitable for real-world production backend development.

---

## 🚀 Features

* 👤 User Registration & Login
* 🔐 JWT Authentication
* 🛡️ Role-Based Access Control (Admin / Teacher / Student)
* 🎓 Student Management (Add Students)
* 📅 Attendance Marking System
* 📊 Attendance Reporting with Filtering

  * Filter by Student ID
  * Filter by Date
  * Combined Filters
* 🔗 MySQL Database Integration (XAMPP)
* 🧱 Clean MVC-like architecture (routes, controllers, models)

---

## 🛠️ Tech Stack

* Python
* Flask
* MySQL (XAMPP)
* Flask-JWT-Extended
* Flask-MySQLdb
* bcrypt (Password hashing)

---

## 📁 Project Structure

```
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
├── models/
│   └── db.py
│
└── middleware/
    └── auth_middleware.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/student-attendance-api.git
cd student-attendance-api
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

* Mac/Linux:

```bash
source venv/bin/activate
```

* Windows:

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install flask flask-mysqldb flask-jwt-extended python-dotenv bcrypt
```

---

### 4️⃣ Setup MySQL (XAMPP)

Create database:

```sql
CREATE DATABASE attendance_system;
```

Create required tables:

* users
* students
* attendance

---

### 5️⃣ Run Project

```bash
python app.py
```

Server runs at:

```
http://127.0.0.1:5000/
```

---

## 📌 API Endpoints

### 🔐 Authentication

* POST `/auth/register`
* POST `/auth/login`

### 🎓 Students

* POST `/student/add` (Admin only)

### 📅 Attendance

* POST `/attendance/mark` (Teacher only)
* GET `/attendance/report` (Filtered + Protected)

---

## 📊 Attendance Filtering

### Examples:

```
/attendance/report?student_id=1
/attendance/report?date=2026-05-08
/attendance/report?student_id=1&date=2026-05-08
```

---

## 🛡️ Role-Based Access

| Role    | Permissions     |
| ------- | --------------- |
| Admin   | Add students    |
| Teacher | Mark attendance |
| Student | View reports    |

---

## 🧪 Sample Login

```json
{
  "email": "admin@gmail.com",
  "password": "123456"
}
```

---

## 🚀 Future Improvements

* Frontend dashboard (React / HTML)
* Deployment (Render / Railway)
* Email notifications
* Attendance analytics dashboard

---

## 👨‍💻 Author

**Bhathiya Abeysinghe**
Computer Science Graduate
Focused on Backend Development & API Systems

---

## ⭐ Note

If you like this project, please consider starring the repository.
