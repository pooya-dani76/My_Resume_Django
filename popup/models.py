from django.db import models

# Create your models here.

class ConsultModel(models.Model):
    name = models.CharField(max_length=300, verbose_name="Your Name")
    email = models.EmailField(verbose_name="Your Email")
    message = models.TextField(verbose_name="Your Message")

    def __str__(self):
        return f"<<{self.name}: {self.message}>>"
    
    class Meta:
        db_table = "consults"
        verbose_name = "Consult"
        verbose_name_plural = "Consults"