from django.db import models


class Ganison(models.Model):
    school_name = models.CharField(max_length=200)
    year = models.IntegerField()
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    year_level = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    answers = models.CharField(max_length=100)
    correct_answers = models.CharField(max_length=100)
    question_number = models.IntegerField()
    subject_contents = models.CharField(max_length=100)
    assessment_areas = models.CharField(max_length=100)
    sydney_correct_count_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    sydney_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    sydney_participants = models.IntegerField()
    student_score = models.DecimalField(max_digits=5, decimal_places=2)
    student_total_assessed = models.IntegerField()
    student_area_assessed_score = models.DecimalField(max_digits=5, decimal_places=2)
    total_area_assessed_score = models.DecimalField(max_digits=5, decimal_places=2)
    participant = models.IntegerField()
    correct_answer_percentage_per_class = models.DecimalField(max_digits=5, decimal_places=2)
    average_score = models.DecimalField(max_digits=5, decimal_places=2)
    school_percentile = models.IntegerField()
    sydney_percentile = models.IntegerField()
    strength_status = models.CharField(max_length=100)
    high_distinct_count = models.IntegerField()
    distinct_count = models.IntegerField()
    credit_count = models.IntegerField()
    participant_count = models.IntegerField()
    award = models.CharField(max_length=100)


class School(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100)

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=100)

class AssessmentAreas(models.Model):
    id = models.AutoField(primary_key=True)
    assessment_areas = models.CharField(max_length=100)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    answers = models.CharField(max_length=100)

class Awards(models.Model):
    id = models.AutoField(primary_key=True)
    award = models.CharField(max_length=100)

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    subject_contents = models.CharField(max_length=100)
