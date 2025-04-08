from django.urls import path
from .import views

urlpatterns = [
    path('trainees/', views.trainee_list, name='trainee_list'),
    # path('trainees/<int:pk>/', views.trainee_detail, name='trainee_detail'),
]
# Compare this snippet from Practice/practiceDay11/practiceDay11/urls.py: