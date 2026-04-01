# 🚀 Job Application Tracker API

A scalable backend system built using **FastAPI** to manage and track job applications across multiple stages with secure authentication.

---

## 📌 Overview

The Job Application Tracker API allows users to:

* Register and authenticate securely using JWT
* Track job applications across different statuses
* Perform full CRUD operations on job entries
* Organize and monitor job search progress efficiently

---

## 🧠 Key Features

* 🔐 **JWT Authentication** (Login & Protected Routes)
* 📋 **Job Management System**

  * Create, Read, Update, Delete jobs
* 🔍 **Filtering & Query Support**
* 📄 **Pagination-ready structure**
* 🧱 **Modular Architecture** (routers, models, schemas)
* ⚡ Built with **FastAPI for high performance APIs**

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python)
* **Database:** SQLite (can be upgraded to PostgreSQL)
* **ORM:** SQLAlchemy
* **Authentication:** JWT (python-jose)
* **Migrations:** Alembic
* **Validation:** Pydantic

---

## 📂 Project Structure

```
job-tracker-api/
│
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   └── jobs.py
│   ├── models/
│   ├── schemas/
│   ├── database.py
│   └── utils/
│
├── main.py
├── requirements.txt
└── Dockerfile
```

---

## 🔑 API Endpoints

### Auth Routes

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| POST   | /auth/register | Register new user |
| POST   | /auth/login    | Login & get token |

---

### Job Routes (Protected)

| Method | Endpoint   | Description  |
| ------ | ---------- | ------------ |
| GET    | /jobs/     | Get all jobs |
| POST   | /jobs/     | Create job   |
| PUT    | /jobs/{id} | Update job   |
| DELETE | /jobs/{id} | Delete job   |

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/your-username/job-application-tracker-api.git
cd job-application-tracker-api

pip install -r requirements.txt
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

