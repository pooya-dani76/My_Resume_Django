# Generated by Django 5.0.3 on 2024-03-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_module', '0003_workshowcasemodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshowcasemodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True, verbose_name='Slug'),
        ),
    ]
