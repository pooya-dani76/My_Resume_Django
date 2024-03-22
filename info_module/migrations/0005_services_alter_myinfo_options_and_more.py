# Generated by Django 5.0.3 on 2024-03-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_module', '0004_alter_myinfo_resume_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('short_description', models.TextField(verbose_name='Short Description')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'db_table': 'services',
            },
        ),
        migrations.AlterModelOptions(
            name='myinfo',
            options={'verbose_name': 'My Info', 'verbose_name_plural': 'Infos'},
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='resume_file',
            field=models.FileField(upload_to='files/me', verbose_name='Resume'),
        ),
    ]
