from django.shortcuts import render
from App1.models import Trainee
# Create your views here.


def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'temp/trainee_list.html', {'trainees': trainees})