from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import StudentForm, SummaryForm
from .models import Summary, School, Student, Subject, AssessmentAreas

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

def dashboard(request):
    context = {
        'schools': School.objects.all(),
        'students': Student.objects.all(),
        'summaries': Summary.objects.all(),
        'subjects': Subject.objects.all(),
        'assessment_areas': AssessmentAreas.objects.all(),
    }
    return render(request, 'core/dashboard.html', context)