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
Company & Department
[Company] 1:N [Department]
id (PK)
name
address
created_at

[Department]
id (PK)
company_id (FK → Company.id)
name
manager_id (FK → Employee.id, nullable)
created_at

Employee
[Employee]
id (PK)
employee_code
first_name
last_name
email
phone
date_of_birth
hire_date
job_title
department_id (FK → Department.id)
manager_id (FK → Employee.id, nullable)  # self-relation
status
current_salary
created_at
updated_at

Employee Related Models
[EmployeeAddress]
id (PK)
employee_id (FK → Employee.id)
address_line
city
country
is_primary

[EmployeeDocument]
id (PK)
employee_id (FK → Employee.id)
doc_type
file_path/url
uploaded_by (FK → UserAccount.id)
uploaded_at
status

[OnboardingTask]
id (PK)
employee_id (FK → Employee.id)
title
description
assigned_to (FK → UserAccount.id, nullable)
due_date
status
completed_at

Users, Roles & Permissions
[UserAccount]
id (PK)
employee_id (FK → Employee.id, nullable)
username
email
password_hash
is_active
created_at
   │
   │ M:N (via RolePermission)
   ▼
[Role]
id (PK)
name
description
   │
   │ M:N (via RolePermission)
   ▼
[Permission]
id (PK)
codename
description

[RolePermission]
id (PK)
role_id (FK → Role.id)
permission_id (FK → Permission.id)

Audit Logs
[AuditLog]
id (PK)
actor_id (FK → UserAccount.id)
action
target_type
target_id
timestamp
details (json)

⚙️ Installation & Setup
# Clone project
git clone https://github.com/USERNAME/ems-backend.git
cd ems-backend

# Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

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
