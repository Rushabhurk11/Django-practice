from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def show_datetime(request):
    now = datetime.now()
    return HttpResponse(f"Current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}")


