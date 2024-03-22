from django.db import models

class MyInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    title = models.TextField(verbose_name="Title(s)")
    available_for_freelancing = models.BooleanField(verbose_name="Available For Freelancing")
    image = models.ImageField(upload_to='images/me', verbose_name="Image")
    years_experience = models.IntegerField(verbose_name="Experience(year)")
    satisfied_customers = models.IntegerField(verbose_name="Satisfied Customers")
    resume_file = models.FileField(upload_to='files/me', verbose_name="Resume")
    is_active = models.BooleanField(verbose_name="Is Active")

    def __str__(self):
        return f"{self.name} --> {self.title}"

    class Meta:
        db_table = "my_info"
        verbose_name = "My Info"
        verbose_name_plural = "Infos"


class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    short_description = models.TextField(verbose_name="Short Description")  

    def __str__(self):
        return self.title

    class Meta:
        db_table = "services"
        verbose_name = "Service"
        verbose_name_plural = "Services"          