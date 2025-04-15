from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

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
