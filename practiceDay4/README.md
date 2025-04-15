# Django Multi-Function App Project

This Django project includes a single app called `utility_app` that handles multiple functionalities through different views.

---

## 🗂 Project Structure

- **Project Name:** `multiviewproject`
- **App Name:** `utility_app`
- **Functionalities:**
  - Show current date and time
  - Return time-based greeting
  - Display a random motivational quote
  - Return the square of a given number via query parameter

---

## 🛠 Setup Instructions

### 1. Create the Project and App
```bash
django-admin startproject multiviewproject
cd multiviewproject
python manage.py startapp utility_app
```

### 2. Register App
Edit `multiviewproject/settings.py` and add the app:
```python
INSTALLED_APPS = [
    ...
    'utility_app',
]
```

---

## 💡 Views in `utility_app/views.py`
```python
from django.http import HttpResponse
from datetime import datetime
import random

def show_datetime(request):
    now = datetime.now()
    return HttpResponse(f"Current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def greet_user(request):
    hour = datetime.now().hour
    if 5 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon!"
    elif 17 <= hour < 21:
        greeting = "Good Evening!"
    else:
        greeting = "Good Night!"
    return HttpResponse(greeting)

def random_quote(request):
    quotes = [
        "Believe in yourself.",
        "You can do it!",
        "Stay positive.",
        "Work hard and stay humble.",
        "Keep going, you're doing great!"
    ]
    return HttpResponse(random.choice(quotes))

def square_number(request):
    try:
        num = int(request.GET.get('number', 0))
        return HttpResponse(f"The square of {num} is {num ** 2}")
    except ValueError:
        return HttpResponse("Invalid number provided.")
```

---

## 🌐 URL Configuration

Edit `multiviewproject/urls.py`:
```python
from django.contrib import admin
from django.urls import path
from utility_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datetime/', views.show_datetime),
    path('greet/', views.greet_user),
    path('quote/', views.random_quote),
    path('square/', views.square_number),  # use like: /square/?number=5
]
```

---

## 🚀 Run the Server
```bash
python manage.py runserver
```

---

## 🔍 Test the Endpoints

- `http://127.0.0.1:8000/datetime/` → Shows current date and time
- `http://127.0.0.1:8000/greet/` → Returns a greeting based on time
- `http://127.0.0.1:8000/quote/` → Returns a random motivational quote
- `http://127.0.0.1:8000/square/?number=5` → Returns square of 5

---

## ✅ You're all set!
This single-app Django project is ready to handle multiple functional routes!