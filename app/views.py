from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .models import Candidate, Profile, Job

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password doesnt exist')

    return render(request, 'app/login.html')

def register_user(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()     

            role = request.POST.get('role')
            profile = Profile.objects.create(owner=user, role=role)
            profile.save()

            if role == 'Candidate':
                candidate = Candidate.objects.create(owner=profile)
                candidate.save()

            return redirect('home')

    ctx = {'form': form}
    return render(request, 'app/register.html', ctx)

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    jobs = Job.objects.all()
    ctx = {'jobs': jobs}
    return render(request, 'app/index.html', ctx )

def about(request):
    return render(request, 'app/about.html' )

def contact(request):
    return render(request, 'app/contact.html' )

def user_role(request):
    user = request.user
    profile = Profile.objects.get(owner = user)
    ctx = {'profile': profile}
    return render(request, 'nav.html', ctx)

def jobs(request):
    jobs = Job.objects.all()
    ctx = {'jobs': jobs}
    return render(request, 'app/jobs.html', ctx)

def job_details(request, name):
    job = Job.objects.get(title = name)
    ctx = {'job': job}
    return render(request, 'app/job-details.html', ctx)

def employer_details(request, name):
    employer = Job.objects.get(recruiter__owner__username = name)
    ctx = {'employer':employer}
    return render(request, 'app/employer-details.html', ctx)

def candidates(request):
    candidates = Candidate.objects.all()
    ctx = {'candidates': candidates}
    return render(request, 'app/candidates.html', ctx)

def candidate_details(request, name):
    candidate = Candidate.objects.get(owner__owner__username = name)
    ctx = {'candidate': candidate}
    return render(request, 'app/candidate-details.html', ctx)
