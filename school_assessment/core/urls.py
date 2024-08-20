from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schools/', views.school_list, name='school_list'),
    path('students/', views.student_list, name='student_list'),
    path('summaries/', views.summary_list, name='summary_list'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_summary/', views.add_summary, name='add_summary'),
    path('dashboard/', views.dashboard, name='dashboard'),
]