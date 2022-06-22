from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
ROLE = (
    ('Client','Client'),
    ('Candidate','Candiate')
)

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    full_name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(blank=True)
    profile_pic = CloudinaryField('Profile', blank = True)
    role = models.CharField(max_length=200, choices=ROLE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username

class JobCategory(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
       return self.type

class JobExperience(models.Model):
    level = models.CharField(max_length=255)

    def __str__(self):
       return self.level
       
class Job(models.Model):
    recruiter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    type = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True)
    experience = models.ForeignKey(JobExperience, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=255)
    pay = models.CharField(max_length=255)
    candidate_gender = models.CharField(max_length=300, default='Male or Female', blank=True)
    description = models.TextField()
    duration = models.CharField(max_length=255, default='1 day', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['-date_posted']