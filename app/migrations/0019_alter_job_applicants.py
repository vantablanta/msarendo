# Generated by Django 4.0.5 on 2022-06-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_job_applicants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='applicants',
            field=models.ManyToManyField(blank=True, to='app.candidate'),
        ),
    ]
