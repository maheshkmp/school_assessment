from django.contrib import admin
from .models import Ganison,School,Class,AssessmentAreas,Student,Answers,Awards,Subject
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Ganison,ImportExportModelAdmin)
admin.site.register(School,ImportExportModelAdmin)
admin.site.register(Class,ImportExportModelAdmin)
admin.site.register(AssessmentAreas,ImportExportModelAdmin)
admin.site.register(Student,ImportExportModelAdmin)
admin.site.register(Answers,ImportExportModelAdmin)
admin.site.register(Awards,ImportExportModelAdmin)
admin.site.register(Subject,ImportExportModelAdmin)

