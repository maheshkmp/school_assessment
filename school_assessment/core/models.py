from django.db import models

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=100)

class AssessmentAreas(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)

class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    answers = models.TextField()

class Awards(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    subject_score = models.FloatField()

class Summary(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_participant = models.IntegerField()
    sydney_percentile = models.FloatField()
    assessment_area_id = models.ForeignKey(AssessmentAreas, on_delete=models.CASCADE)
    award_id = models.ForeignKey(Awards, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.FloatField()
    correct_answer = models.CharField(max_length=255)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    participant = models.BooleanField()
    student_score = models.FloatField()
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=50)
    answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)
    correct_answer_id = models.IntegerField()