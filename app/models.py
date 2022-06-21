from django.db import models
from django.contrib.auth.models import User

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
    role = models.CharField(max_length=200, choices=ROLE)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username