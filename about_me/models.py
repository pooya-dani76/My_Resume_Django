from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class AbilitiesModel(models.Model):
    name = models.CharField(max_length=300, verbose_name="Ability Name")
    mastery = models.IntegerField(verbose_name="Mastery Amount(Percentage)",
                                  validators=[MaxValueValidator(100), MinValueValidator(1)])
    is_active = models.BooleanField(verbose_name="is Active")

    def __str__(self):
        return f"{self.name}({self.mastery}%)"

    class Meta:
        db_table = "abilities"
        verbose_name = "Ability"
        verbose_name_plural = "Abilities"


class EducationModel(models.Model):
    degree_choices = [
        (1, "High School"),
        (2, "Bachelor"),
        (3, "Master")]
    university = models.CharField(max_length=200, verbose_name="University")
    start_year = models.IntegerField(verbose_name="Start Year")
    finish_year = models.IntegerField(null=True, blank=True, verbose_name="Finish Year")
    degree = models.IntegerField(choices=degree_choices)
    short_description = models.TextField(verbose_name="Short Description")
    is_active = models.BooleanField(verbose_name="is Active")

    def __str__(self):
        return self.university
    
    class Meta:
        db_table = "Education"
        verbose_name = "Education"
        verbose_name_plural = "Educations"
