from django.contrib import admin
from . import models

# Register your models here.


class InfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'available_for_freelancing', 'is_active']
    list_editable = ['is_active', 'available_for_freelancing']
    list_display_links = ['name']


admin.site.register(models.MyInfoModel, InfoAdmin)
