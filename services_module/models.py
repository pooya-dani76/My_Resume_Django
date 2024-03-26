from django.db import models

# Create your models here.


class ServicesModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    short_description = models.TextField(verbose_name="Short Description")
    logo = models.ImageField(upload_to="uploads/logos", null=True, verbose_name="Service Logo")
    is_active = models.BooleanField(default=False, verbose_name="Is Active") 
    svg_code = models.TextField(null=True, blank=True, verbose_name="Svg File Html Code") 

    def __str__(self):
        return self.title

    class Meta:
        db_table = "services"
        verbose_name = "Service"
        verbose_name_plural = "Services" 