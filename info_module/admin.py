from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.MyInfoModel)
admin.site.register(models.ServicesModel)
admin.site.register(models.WorkShowCaseModel)