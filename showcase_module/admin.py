from django.contrib import admin
from . import models

class WorkShowCaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'is_active']
    list_editable = ['is_active']
    list_display_links = ['title']


admin.site.register(models.WorkShowCaseModel, WorkShowCaseAdmin)
admin.site.register(models.WorkCategory)
