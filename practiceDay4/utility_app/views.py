from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

# Create your views here.


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
