from django.db import models

# Create your models here.

class ArticleModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    date = models.DateField(auto_now_add=True, editable=False, verbose_name='Date of Article')
    image = models.ImageField(upload_to="uploads/articles", null=True, blank=True, verbose_name="Image")
    is_active = models.BooleanField(verbose_name="is active")

    def __str__(self):
        return f"{self.title} --> {self.date}"

    class Meta:
        db_table = "article"
        verbose_name = "Article"
        verbose_name_plural = "Articles"