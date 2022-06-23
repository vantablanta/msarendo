from django.contrib import admin
from .models import Profile, Job, JobCategory, JobExperience, Candidate, AppliedJobs
# Register your models here.

admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(JobCategory)
admin.site.register(JobExperience)
admin.site.register(Candidate)
admin.site.register(AppliedJobs)