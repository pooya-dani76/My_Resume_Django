# Generated by Django 5.0.3 on 2024-03-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkShowCaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/works', verbose_name='Banner Image')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Work Show Case',
                'verbose_name_plural': 'Work Show Cases',
                'db_table': 'work_show_case',
            },
        ),
    ]
