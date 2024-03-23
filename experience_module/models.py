from django.db import models

# Create your models here.


class WorkExperienceModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    work_place = models.CharField(max_length=200, verbose_name="Company")
    start_year = models.IntegerField(verbose_name="Start Year")
    finish_year = models.IntegerField(verbose_name="Finish Year", blank=True, null=True)
    short_description = models.TextField(verbose_name="Short Description")
    is_active = models.BooleanField(default=False, verbose_name="Is Active")

    def __str__(self):
        return f"{self.title} in {self.work_place}"

    class Meta:
        db_table = "work_experience"
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experiences" 