# Day 1
# 🧱 Django Project Structure & File Explanation

This guide walks you through creating a Django project step-by-step and explains the purpose of each file and folder.

---

## ✅ Step 1: Set Up the Environment

1. **Create a project folder**:
   ```bash
   mkdir myproject
   cd myproject
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/macOS
   env\Scripts\activate     # Windows
   ```

3. **Install Django**:
   ```bash
   pip install django
   ```

4. *(Optional)* Install extras:
   ```bash
   pip install mysqlclient faker django-extensions
   ```

---

## ✅ Step 2: Create the Django Project

```bash
django-admin startproject myproject .
```

This creates the following structure:

```
myproject/
├── manage.py
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 📂 Explanation of Project Structure

### ▶ Outer `myproject/` (Project Root)

- **`manage.py`**  
  Command-line utility for Django commands like:
  - `runserver`
  - `migrate`
  - `createsuperuser`
  - `startapp`

---

### ▶ Inner `myproject/` (Settings Folder)

- **`__init__.py`**  
  Marks this folder as a Python package.

- **`settings.py`**  
  The core configuration file:
  - Installed apps
  - Database settings
  - Static files
  - Middleware
  - Templates
  - Allowed hosts

- **`urls.py`**  
  Maps URLs to views. Acts like a **traffic controller**.

- **`wsgi.py`**  
  Used to deploy the app on WSGI servers like Gunicorn, Apache.

- **`asgi.py`**  
  Supports async deployment using ASGI servers like Daphne, Uvicorn.

---

## ✅ Step 3: Run the Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

You're now ready to start creating apps and building your project further! 🚀
