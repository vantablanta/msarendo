from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import  Profile, Job


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, label='',widget=forms.EmailInput(attrs={'class': 'form-control mb-4', 'placeholder': 'email'}))
    username =forms.CharField(max_length=200, label='',widget=forms.TextInput(attrs={'class': 'form-control mb-4','placeholder': 'username'}))
    password1 = forms.CharField(max_length=200,label='',widget=forms.PasswordInput(attrs={'class': 'form-control mb-4', 'placeholder': 'password'}))
    password2 = forms.CharField(max_length=200, label='',widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','placeholder': 'confirm password'}))
    
    class Meta():
       model=User
       fields = ['email', 'username', 'password1', 'password2']


class PostJobForm(ModelForm):
    title =forms.CharField(max_length=200, label='',widget=forms.TextInput(attrs={'class': 'form-control mb-4','placeholder': 'job title'}))
    location =forms.CharField(max_length=200, label='',widget=forms.TextInput(attrs={'class': 'form-control mb-4','placeholder': 'location'}))
    pay =forms.CharField(max_length=200, label='',widget=forms.TextInput(attrs={'class': 'form-control mb-4','placeholder': 'pay'}))
    candidate_gender =forms.CharField(max_length=200, label='',widget=forms.TextInput(attrs={'class': 'form-control mb-4','placeholder': 'male or female'}))
    description =forms.CharField(label='',widget=forms.Textarea(attrs={'class': 'form-control mb-4','placeholder': 'description'}))
    duration =forms.CharField(max_length=200, label='',widget=forms.TextInput(attrs={'class': 'form-control mb-4','placeholder': 'duration i.e 1 day'}))
    class Meta():
        model=Job
        fields = ['title', 'type', 'experience', 'location', 'pay',
        'candidate_gender', 'description', 'duration', ]
        labels = {
            "type": "select job category",
            "experience": 'select candidate experience'

        }
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control mb-4 '}),
            'experience': forms.Select(attrs={'class': 'form-control mb-4 '})
        }


class UpdateProfileForm(ModelForm):
    full_name = forms.CharField(max_length=200, label='Full name',widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    location = forms.CharField(max_length=200, label='location',widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    about = forms.CharField(max_length=200, label='about',widget=forms.Textarea(attrs={'class': 'form-control mb-4'}))
    profile_pic = forms.FileField(max_length=200,label='upload profile photo',widget=forms.FileInput(attrs={'class': 'form-control mb-4'}))
    
    class Meta():
        model = Profile
        fields = ['full_name', 'location', 'about', 'profile_pic']
