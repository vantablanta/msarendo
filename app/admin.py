from django.contrib import admin
from .models import Profile, Job, JobCategory, JobExperience
# Register your models here.

admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(JobCategory)
admin.site.register(JobExperience)