from django.contrib import admin

from .models import Ganison

from import_export.admin import ImportExportModelAdmin

admin.site.register(Ganison, ImportExportModelAdmin)





