# Generated by Django 4.0.5 on 2022-06-22 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_jobcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.jobcategory'),
        ),
    ]