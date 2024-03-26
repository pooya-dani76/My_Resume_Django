from django.contrib import admin
from . import models

# Register your models here.

class AbilitiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'mastery', 'is_active']
    list_editable = ['is_active']
    list_display_links = ['name']


class EducationAdmin(admin.ModelAdmin):
    list_display = ['university', 'degree', 'is_active']
    list_editable = ['is_active']
    list_display_links = ['university']


admin.site.register(models.AbilitiesModel, AbilitiesAdmin)
admin.site.register(models.EducationModel, EducationAdmin)