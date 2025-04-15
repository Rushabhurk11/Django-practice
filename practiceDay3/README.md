# Django Time-Based Project

This Django project includes two simple apps:

1. **datetime_app** – Displays the current date and time.
2. **greeting_app** – Returns a greeting based on the current time (Good Morning, Afternoon, Evening, or Night).

---

## 🔧 Setup Instructions

### 1. Create the Project
```bash
django-admin startproject timeproject
cd timeproject
```

### 2. Create the Apps
```bash
python manage.py startapp datetime_app
python manage.py startapp greeting_app
```

### 3. Register Apps in `settings.py`
Open `timeproject/settings.py` and add the apps:

```python
INSTALLED_APPS = [
    ...
    'datetime_app',
    'greeting_app',
]
```

---

## 🧠 App Logic

### `datetime_app/views.py`
```python
from django.http import HttpResponse
from datetime import datetime

def show_datetime(request):
    now = datetime.now()
    return HttpResponse(f"Current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}")
```

---

### `greeting_app/views.py`
```python
from django.http import HttpResponse
from datetime import datetime

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
```

---

## 🌐 URL Configuration

All URLs are defined in the main `urls.py` file.

### `timeproject/urls.py`
```python
from django.contrib import admin
from django.urls import path
from datetime_app.views import show_datetime
from greeting_app.views import greet_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datetime/', show_datetime),
    path('greet/', greet_user),
]
```

---

## 🚀 Run the Server
```bash
python manage.py runserver
```

### Test the Endpoints:
- `http://127.0.0.1:8000/datetime/` → Shows current date and time.
- `http://127.0.0.1:8000/greet/` → Returns time-based greeting.

---

## ✅ Done!
You're all set with a simple Django project with two functional views.