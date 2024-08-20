from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schools/', views.school_list, name='school_list'),
    path('students/', views.student_list, name='student_list'),
    path('summaries/', views.summary_list, name='summary_list'),
]