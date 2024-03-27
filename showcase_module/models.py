from django.db import models
from django.urls import reverse

# Create your models here.

class WorkCategory(models.Model):
    name = models.CharField(max_length=300, verbose_name="Category Name") 
    is_active = models.BooleanField(default=False, verbose_name="Is Active") 

    def __str__(self):
        return self.name  

    class Meta:
        db_table = "work_category"
        verbose_name = "Work Category"
        verbose_name_plural = "Work Categories"  



class WorkShowCaseModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    short_description = models.TextField(verbose_name="Short Description")
    image = models.ImageField(upload_to='images/works',null=True, blank=True, verbose_name="Banner Image") 
    date = models.DateField(null=True, blank=True, verbose_name='Creation Date') 
    description = models.TextField(null=True, blank=True, verbose_name="Explain More About Project") 
    link = models.URLField(max_length=300, null=True, blank=True, verbose_name="Project Url")
    main_technology = models.CharField(max_length=200, null=True, blank=True, verbose_name="Project Main Technology")
    category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Category")
    slug = models.SlugField(null=False, db_index=True, unique=True, blank=True, max_length=200, verbose_name='Slug')
    is_active = models.BooleanField(default=False, verbose_name="Is Active")

    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "work_show_case"
        verbose_name = "Work Show Case"
        verbose_name_plural = "Work Show Cases"      