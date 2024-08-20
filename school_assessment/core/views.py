from django.shortcuts import render
from .models import Summary, School, Student

def home(request):
    return render(request, 'core/home.html')

def school_list(request):
    schools = School.objects.all()
    return render(request, 'core/school_list.html', {'schools': schools})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

def summary_list(request):
    summaries = Summary.objects.all()
    return render(request, 'core/summary_list.html', {'summaries': summaries})