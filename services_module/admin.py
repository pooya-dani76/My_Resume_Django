from django.contrib import admin
from . import models

# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']
    list_display_links = ['title']

admin.site.register(models.ServicesModel, ServicesAdmin)
