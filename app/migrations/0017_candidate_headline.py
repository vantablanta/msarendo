# Generated by Django 4.0.5 on 2022-06-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='headline',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]