# Generated by Django 5.0.3 on 2024-03-26 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services_module', '0003_servicesmodel_svg_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicesmodel',
            name='logo',
        ),
    ]