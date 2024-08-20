import csv
from django.core.management.base import BaseCommand
from core.models import School, Class, AssessmentAreas, Student, Answers, Awards, Subject, Summary

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        with open('path/to/your/csv/file.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Create School
                school, _ = School.objects.get_or_create(name=row['school_name'])
                
                # Create Class
                class_obj, _ = Class.objects.get_or_create(class_name=row['Class'])
                
                # Create AssessmentAreas
                assessment_area, _ = AssessmentAreas.objects.get_or_create(name=row['Assessment Areas'])
                
                # Create Student
                student, _ = Student.objects.get_or_create(
                    fullname=f"{row['First Name']} {row['Last Name']}"
                )
                
                # Create Answers
                answers, _ = Answers.objects.get_or_create(answers=row['Answers'])
                
                # Create Subject
                subject, _ = Subject.objects.get_or_create(
                    subject=row['Subject'],
                    subject_score=float(row['student_score'])
                )
                
                # Create Summary
                Summary.objects.create(
                    school_id=school,
                    sydney_participant=int(row['sydney_participants']),
                    sydney_percentile=float(row['sydney_average_score']),
                    assessment_area_id=assessment_area,
                    class_id=class_obj,
                    correct_answer_percentage_per_class=float(row['sydney_correct_count_percentage']),
                    correct_answer=row['Correct Answers'],
                    student_id=student,
                    participant=True,  
                    student_score=float(row['student_score']),
                    subject_id=subject,
                    year_level_name=row['Year Level'],
                    answer_id=answers,
                    
                    category_id=1,  
                    correct_answer_id=1,  
                    award_id=Awards.objects.first()  
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))