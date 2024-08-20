from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import StudentForm, SummaryForm
from .models import Summary, School, Student

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def school_list(request):
    schools = School.objects.all()
    return render(request, 'core/school_list.html', {'schools': schools})

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

@login_required
def summary_list(request):
    summaries = Summary.objects.all()
    return render(request, 'core/summary_list.html', {'summaries': summaries})


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/add_student.html', {'form': form})

@login_required
def add_summary(request):
    if request.method == 'POST':
        form = SummaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('summary_list')
    else:
        form = SummaryForm()
    return render(request, 'core/add_summary.html', {'form': form})