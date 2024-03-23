from django.db import models

# Create your models here.


class WorkShowCaseModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    short_description = models.TextField(verbose_name="Short Description")
    image = models.ImageField(upload_to='images/works',null=True, blank=True, verbose_name="Banner Image")  
    is_active = models.BooleanField(default=False, verbose_name="Is Active")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "work_show_case"
        verbose_name = "Work Show Case"
        verbose_name_plural = "Work Show Cases"