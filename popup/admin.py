from django.contrib import admin
from . import models

# Register your models here.

class ConsultAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_display_links = ['name']


admin.site.register(models.ConsultModel, ConsultAdmin)