EMS – Employee Management System (Backend)

Tech Stack: Django REST Framework + JWT Authentication

نظام لإدارة الموظفين داخل الشركات (Employee Management System). يوفر النظام تسجيل الدخول، إدارة الموظفين، إدارة الحسابات والصلاحيات، ومتابعة العمليات الإدارية.

✨ Features

🔐 JWT Authentication (Login + Protected APIs)

👤 User Accounts Management

🛡️ Roles & Permissions System

📋 Employees CRUD

🧩 Modular Architecture

🗄️ PostgreSQL / SQLite Support

🌐 CORS Enabled

📦 Production-ready settings structure

🏗️ Project Structure
ems-backend/
│── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│── ems/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   ├── urls.py
│   └── utils/
│
│── env/
│── manage.py

🗄️ ERD (Entity Relationship Diagram)
![ERD](img/ERD.png)


# Install Dependencies
pip install -r requirements.txt

# Apply Migrations
python manage.py migrate

# Create Superuser
python manage.py createsuperuser

# Run Server
python manage.py runserver

🔐 Authentication (JWT)

Login Endpoint:

POST /api/auth/login/


Request Body:

{
  "username": "eslam",
  "password": "12345678"
}


Response:

{
  "access": "JWT_TOKEN",
  "refresh": "REFRESH_TOKEN"
}

📡 API Endpoints
Method	Endpoint	Description	Protected
POST	/api/auth/login/	Login (JWT)	No
GET	/api/employees/	List All Employees	Yes
POST	/api/employees/	Create Employee	Yes
GET	/api/employees/:id/	Retrieve Employee	Yes
PUT	/api/employees/:id/	Update Employee	Yes
DELETE	/api/employees/:id/	Delete Employee	Yes
GET	/api/users/permissions/	Get Logged User Permissions	Yes

ملاحظة: جميع Endpoints الخاصة بالـ CRUD تتطلب JWT Token صالح في الهيدر Authorization: Bearer <token>.
