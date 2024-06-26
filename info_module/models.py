from django.db import models

class MyInfoModel(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    age = models.IntegerField(blank=True, null=True, verbose_name="Age")
    image = models.ImageField(upload_to='images/me', verbose_name="Image")
    title = models.TextField(verbose_name="Title(s)")
    about_me = models.TextField(null=True, blank=True, verbose_name="About Me")
    about_me_extra = models.TextField(null=True, blank=True, verbose_name="About Me More")
    phone = models.IntegerField(blank=True, null=True, verbose_name="Phone Number")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    address = models.TextField(blank=True, null=True, verbose_name="Address")
    country = models.CharField(max_length=200, verbose_name="Country")
    linked_in = models.URLField(max_length=300, null=True, blank=True, verbose_name="Linkedin Url")
    instagram = models.URLField(max_length=300, null=True, blank=True, verbose_name="Instagram Url")
    twitter = models.URLField(max_length=300, null=True, blank=True, verbose_name="Twitter Url")
    facebook = models.URLField(max_length=300, null=True, blank=True, verbose_name="Facebook Url")
    years_experience = models.IntegerField(verbose_name="Experience(year)")
    satisfied_customers = models.IntegerField(verbose_name="Satisfied Customers")
    resume_file = models.FileField(upload_to='files/me', verbose_name="Resume")
    available_for_freelancing = models.BooleanField(verbose_name="Available For Freelancing")
    is_active = models.BooleanField(verbose_name="Is Active")

    def __str__(self):
        return f"{self.name} --> {self.title}"

    class Meta:
        db_table = "my_info"
        verbose_name = "My Info"
        verbose_name_plural = "Infos"