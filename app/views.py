from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import RegisterForm
from .models import Profile

# Create your views here.
def login_user(request):
    ctx = {}
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

            return redirect('home')

    ctx = {'form': form}
    return render(request, 'app/register.html', ctx)

def home(request):
    return render(request, 'app/index.html' )

def about(request):
    return render(request, 'app/about.html' )

def contact(request):
    return render(request, 'app/contact.html' )

def jobs(request):
    ctx = {}
    return render(request, 'app/jobs.html')