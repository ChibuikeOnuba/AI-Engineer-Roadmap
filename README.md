# 📘 Project: Full-Stack Blog API with FastAPI and JWT Authentication

> A high-performance, production-ready blog API built using **FastAPI**, complete with **user authentication**, **JWT access tokens**, and **ORM-backed CRUD operations**. This project combines clean architecture, modular routing, and real-world patterns to create a scalable API, perfect for both learning and deploying.

---

## 🚀 Tech Stack

- **FastAPI** – Lightning-fast web framework built on Starlette
- **Pydantic** – Data validation using Python type hints
- **SQLAlchemy** – ORM for PostgreSQL (or SQLite)
- **bcrypt** – Password hashing
- **JWT** – Secure authentication tokens
- **Uvicorn** – ASGI server for local development
- **Swagger & Redoc** – Auto-generated interactive API documentation

---

## 🧠 What we did

This project follows a **step-by-step** approach to build a fully functioning API, covering the following concepts:

- 🌐 Routing, Path & Query Parameters
- 🧾 Request & Response Models using Pydantic
- 🛢️ Database integration with SQLAlchemy
- 📝 CRUD operations for Blog Posts
- 👤 User registration & password hashing
- 🔐 JWT-based user authentication
- ⚡ Route protection and authorization
- 📦 API Modularization with Routers
- 📁 Clean code with Repository Pattern
- 🚀 Deployment Ready

---

## 🗂️ Project Structure

```
📦 fastapi-blog-api
├── 📁 app
│   ├── 📁 routers        # Blog, User, Auth API routes
│   ├── 📁 database       # DB config and session
│   ├── 📁 models         # SQLAlchemy models
│   ├── 📁 schemas        # Pydantic schemas
│   ├── 📁 repository     # CRUD logic separated for scalability
│   ├── 📁 hashing        # Password hashing utilities
│   ├── 📁 auth           # JWT token creation and verification
│   └── main.py          # Entry point of the application
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🛠️ Setup Instructions

1. **Clone the Repo**
   ```bash
   git clone https://github.com/ChibuikeOnuba/AI-Engineer-Roadmap
   cd fastapi blog api
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the Database**
   - Update `DATABASE_URL` in `database.py` if needed.
   - Tables will be auto-created on first run.

5. **Run the App**
   ```bash
   uvicorn main:app --reload
   ```

6. **Explore the API Docs**
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔐 Authentication

- Users register with a hashed password.
- Login returns a **JWT access token**.
- Protected routes require token-based authorization using:
  ```http
  Authorization: Bearer <your_token_here>
  ```

## 🌟 Why FastAPI?

FastAPI combines speed, type safety, and modern development practices to make building robust APIs enjoyable and efficient. Features like auto-generated documentation and data validation make it ideal for building production-ready services.

---

## 🤝 Acknowledgements

This project is based on the excellent [FastAPI Course by Bitfumes](https://www.youtube.com/watch?v=0sOvCWFmrtA). Special thanks to the creator for such a structured walkthrough.

---
