# Generated by Django 4.0.5 on 2022-06-22 07:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_profile_resume_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Profile'),
        ),
    ]
