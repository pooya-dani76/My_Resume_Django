# Generated by Django 5.0.3 on 2024-03-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abilitiesmodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is Active'),
            preserve_default=False,
        ),
    ]
