EMS – Employee Management System (Backend)

 Django REST Framework + JWT Authentication

Overview

Employee Management System (EMS) هو نظام لإدارة الموظفين داخل الشركات.
يوفر النظام إمكانية تسجيل الدخول، عرض الموظفين، إنشاء حسابات جديدة، تحديد الصلاحيات (Roles & Permissions)، ومتابعة العمليات الإدارية.

هذا المستودع يحتوي على الكود الخاص بالـ Backend باستخدام Django REST Framework وبنية نظيفة قابلة للتطوير.

✨ Features

🔐 JWT Authentication (Login + Protected APIs)

👤 User Accounts Management

🛡️ Roles & Permissions System

📋 Employees CRUD

🧩 Modular Architecture

🗄️ PostgreSQL / SQLite Support

🌐 CORS Enabled

📦 Production-ready settings structure

🏗️ Project Architecture
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
[Company] 
  id (PK)
  name
  address
  created_at
     │
     │ 1:N
     ▼
[Department] 
  id (PK)
  company_id (FK → Company.id)
  name
  manager_id (FK → Employee.id, nullable)
  created_at
     │
     │ 1:N
     ▼
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
  manager_id (FK → Employee.id, nullable) ──┐
  status                                     │ self-relation
  current_salary                              │
  created_at                                  │
  updated_at                                  │
     │                                        │
     │ 1:N                                    │
     ▼                                        │
[EmployeeAddress]                             │
  id (PK)                                     │
  employee_id (FK → Employee.id)              │
  address_line                                │
  city                                        │
  country                                     │
  is_primary                                  │
                                              │
[EmployeeDocument] <─┐                        │
  id (PK)            │                        │
  employee_id (FK)───┘                        │
  doc_type                                    │
  file_path/url                               │
  uploaded_by (FK → UserAccount.id)           │
  uploaded_at                                 │
  status                                      │
                                              │
[OnboardingTask]                              
  id (PK)                                    
  employee_id (FK → Employee.id)              
  title                                      
  description                                
  assigned_to (FK → UserAccount.id, nullable)
  due_date                                    
  status                                      
  completed_at                                

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

[AuditLog] 
  id (PK)
  actor_id (FK → UserAccount.id)
  action
  target_type
  target_id
  timestamp
  details (json)

⚙️ Installation & Setup
1️⃣ Clone Project
git clone https://github.com/USERNAME/ems-backend.git
cd ems-backend

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py migrate

5️⃣ Create Superuser
python manage.py createsuperuser

6️⃣ Run Server
python manage.py runserver

🔐 Authentication (JWT)
Login

POST /api/auth/login/

Request:

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
Method	Endpoint	Description
POST	/api/auth/login/	Login (JWT)
GET	/api/employees/	List All Employees (protected)
POST	/api/employees/	Create Employee
GET	/api/employees/:id/	Retrieve Employee
PUT	/api/employees/:id/	Update Employee
DELETE	/api/employees/:id/	Delete Employee
GET	/api/users/permissions/	Get Logged User Permissions
