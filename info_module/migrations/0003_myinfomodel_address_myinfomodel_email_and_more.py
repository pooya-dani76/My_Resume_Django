# Generated by Django 5.0.3 on 2024-03-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_module', '0002_myinfomodel_facebook_myinfomodel_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinfomodel',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='myinfomodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='myinfomodel',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone Number'),
        ),
    ]
