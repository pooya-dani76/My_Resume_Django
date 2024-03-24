from django.contrib import admin
from . import models

# Register your models here.

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'work_place' , 'is_active']
    list_editable = ['is_active']
    list_display_links = ['title']

admin.site.register(models.WorkExperienceModel, WorkExperienceAdmin)