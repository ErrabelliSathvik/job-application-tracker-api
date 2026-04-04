# 🚀 Job Application Tracker API

A **production-style backend system** built with FastAPI to help users track job applications, analyze progress, and manage their job search efficiently.

---

## 📌 Why this project?

Tracking job applications manually is inefficient and error-prone.
This system provides:

* Centralized tracking of applications
* Status lifecycle management (Applied → Interview → Offer → Rejected)
* Secure multi-user environment using JWT authentication

👉 Designed as a **scalable backend system**, not just a CRUD API.

---

## 🧠 Core Features

### 🔐 Authentication & Security

* JWT-based authentication
* Password hashing using bcrypt
* Protected routes with token validation

---

### 📋 Job Application Management

* Create, update, delete job applications
* Track application status lifecycle
* Associate jobs with authenticated users (data isolation)

---

### 📊 Analytics & Insights

* Total applications per user
* Success rate tracking
* Average response time
* Most applied companies

👉 Moves beyond CRUD → provides **decision-making insights**

---

### ⚙️ Backend Design

* Modular architecture (routers, schemas, models)
* Clean separation of concerns
* Scalable structure for future extensions

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Database:** SQLite (easily extensible to PostgreSQL)
* **ORM:** SQLAlchemy
* **Authentication:** JWT (python-jose)
* **Migrations:** Alembic
* **Validation:** Pydantic

---

## 🏗️ System Design

### Architecture Flow

Client → FastAPI → Business Logic → Database

---

### Key Design Decisions

* **JWT Authentication** for stateless scalability
* **Relational DB schema** for structured job tracking
* **User-based data isolation** for multi-user support
* Designed to support:

  * indexing for faster queries
  * caching (Redis - future scope)
  * horizontal scaling

---

## 📂 Project Structure

```
job-tracker-api/
│
├── app/
│   ├── routers/       # API routes (auth, jobs)
│   ├── models/        # Database models
│   ├── schemas/       # Request/response validation
│   ├── database.py    # DB connection
│   └── utils/         # Helper functions
│
├── main.py
├── requirements.txt
└── Dockerfile
```

---

## 🔑 API Endpoints

### Auth Routes

| Method | Endpoint       | Description     |
| ------ | -------------- | --------------- |
| POST   | /auth/register | Register user   |
| POST   | /auth/login    | Login & get JWT |

---

### Job Routes (Protected)

| Method | Endpoint   | Description   |
| ------ | ---------- | ------------- |
| GET    | /jobs/     | Get user jobs |
| POST   | /jobs/     | Create job    |
| PUT    | /jobs/{id} | Update job    |
| DELETE | /jobs/{id} | Delete job    |

---

## 📊 Analytics Endpoint (Key Feature)

### Get Application Insights

```http
GET /analytics
Authorization: Bearer <token>
```

### Sample Response

```json
{
  "total_applications": 42,
  "success_rate": 18.5,
  "avg_response_days": 5,
  "top_companies": ["Amazon", "TCS"]
}
```

### What it provides

* 📈 Total applications tracked per user
* 🎯 Success rate based on offers/interviews
* ⏱️ Average response time from companies
* 🏢 Most frequently applied companies

👉 Enables users to **analyze and improve their job search strategy**

---

## 🌐 Live API

Base URL:
https://your-api.onrender.com

Swagger Docs:
https://your-api.onrender.com/docs

👉 Fully deployed backend with interactive API documentation


---

## 🧪 Sample API Usage

### Login

```json
POST /auth/login

{
  "email": "test@example.com",
  "password": "123456"
}
```

### Response

```json
{
  "access_token": "your_jwt_token"
}
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/ErrabelliSathvik/job-application-tracker-api.git
cd job-application-tracker-api

pip install -r requirements.txt
uvicorn main:app --reload
```

Docs available at:
http://127.0.0.1:8000/docs

---

## 🚀 Future Improvements

* PostgreSQL with indexing
* Redis caching for performance
* Email automation for tracking applications
* AI-based job matching
* Frontend dashboard integration

---

## 📌 What this project demonstrates

* Backend system design
* Authentication & security
* REST API development
* Database modeling
* Scalable architecture thinking

---

## 👤 Author

**Sathvik Errabelli**
