from django import forms
from .models import Student, Summary

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fullname']

class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['school_id', 'student_id', 'subject_id', 'student_score', 'year_level_name']