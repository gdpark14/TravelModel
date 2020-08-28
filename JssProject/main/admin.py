from django.contrib import admin
from .models import Jasosel,Comment,Location
from import_export.admin import ExportActionModelAdmin,ImportExportMixin, ImportMixin

# Register your models here.

admin.site.register(Jasosel)
admin.site.register(Comment)

class LocationAdmin(ImportExportMixin,admin.ModelAdmin):
    pass

admin.site.register(Location,LocationAdmin)