# 🏗️ School Management System — Project Structure & Setup Guide

This document helps every developer quickly set up, understand, and contribute to the **School Management System (SMS)** project, including both **Django (Backend)** and **React (Frontend)** components.

---

## 🚀 0. Developer Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/GoUpTech/school-management-system.git
cd school-management-system
```

### 2️⃣ Setup Branches

* Pull latest branches:

  ```bash
  git fetch --all
  ```
* Switch to development branch:

  ```bash
  git checkout dev
  ```
* Create a feature branch:

  ```bash
  git checkout -b feature/student-dashboard
  ```

### 3️⃣ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend will run on: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

### 4️⃣ Frontend Setup

```bash
cd ../frontend
npm install
npm start
```

Frontend will run on: **[http://localhost:3000](http://localhost:3000)**

### 5️⃣ Start Coding ✨

* Make sure your backend and frontend are both running.
* Implement features only inside your module folder.
* Commit frequently and push your feature branch:

  ```bash
  git add .
  git commit -m "feat: added student dashboard UI"
  git push origin feature/student-dashboard
  ```

---

## 📁 1. Folder Structure Overview

```
school-management-system/
│
├── backend/                         # Django Backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── school_management/            # Project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── apps/                         # All Django apps go here
│   │   ├── accounts/
│   │   ├── students/
│   │   ├── teachers/
│   │   ├── fees/
│   │   └── attendance/
│   │
│   ├── static/                       # Static files (optional)
│   ├── media/                        # Uploaded media (images, docs)
│   └── db.sqlite3 (or use PostgreSQL)
│
├── frontend/                         # React Frontend
│   ├── package.json
│   ├── vite.config.js / next.config.js / webpack.config.js
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── modules/
│   │   │   ├── student-dashboard/
│   │   │   ├── teacher-dashboard/
│   │   │   ├── fees-management/
│   │   │   └── ...
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── services/
│   │   │   └── api.js
│   │   └── App.js
│   └── public/
│
├── docs/                             # Documentation
│   ├── DEVELOPERS_GUIDE.md
│   ├── MODULE_WORKFLOW.md
│   └── API_DOCS.md
│
├── .gitignore
├── README.md
└── LICENSE
```

---

## ⚙️ 2. Backend (Django) Setup

### Install Dependencies

```bash
pip install django djangorestframework django-cors-headersders
pip freeze > requirements.txt
```

### Update `settings.py`

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'corsheaders',
    'accounts',
    'students',
    'teachers',
    'fees',
    'attendance',
]

Add middleware at the very top of the list (before CommonMiddleware):

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...,
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React dev server
]
```

### Example API (`students/views.py`)

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def student_dashboard(request):
    data = {
        "name": "Sam Gupta",
        "attendance": 92,
        "upcoming_classes": 3
    }
    return Response(data)
```

---

## 🎨 3. Frontend (React) Setup

### Example API Configuration (`frontend/src/services/api.js`)

```javascript
import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

export default API;
```

### Example Component (`frontend/src/modules/student-dashboard/index.jsx`)

```javascript
import React, { useEffect, useState } from "react";
import API from "../../services/api";

export default function StudentDashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    API.get("/students/dashboard/")
      .then((res) => setData(res.data))
      .catch((err) => console.error(err));
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div className="p-4">
      <h2>Welcome, {data.name}</h2>
      <p>Attendance: {data.attendance}%</p>
      <p>Upcoming Classes: {data.upcoming_classes}</p>
    </div>
  );
}
```

---

## 🔗 4. Integration (Backend ↔ Frontend)

### Django `urls.py`

```python
from django.urls import path
from students.views import student_dashboard

urlpatterns = [
    path('api/students/dashboard/', student_dashboard, name='student_dashboard'),
]
```

### React Axios

* Communicates with Django API endpoints (port 8000)
* Django CORS settings allow requests from React (port 3000)

---

## 🧪 5. Running in Development

### Backend

```bash
cd backend
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm start
```

* Backend → `http://127.0.0.1:8000`
* Frontend → `http://localhost:3000`

---

## 🚀 6. Production Integration

For deployment:

* Build React app → `npm run build`
* Serve React build via Django or Nginx

Example:

```
frontend/build/ → static files (served by Nginx)
Django → runs REST APIs (Gunicorn/Uvicorn)
```

---

## ✅ Summary Table

| Layer       | Tech         | Port | Purpose                    |
| ----------- | ------------ | ---- | -------------------------- |
| Backend     | Django + DRF | 8000 | APIs, Auth, Database       |
| Frontend    | React.js     | 3000 | UI, API Calls              |
| Integration | Axios + CORS | —    | Communication between both |

---

> 📘 **Note:** Keep each module (Accounts, Students, Teachers, Fees, Attendance) in its own Django app and React folder for better maintainability.
