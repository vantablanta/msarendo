from django.shortcuts import render

# Create your views here.
def login_user(request):
    ctx = {}
    return render(request, 'app/login.html')

def register_user(request):
    ctx = {}
    return render(request, 'app/register.html')

def home(request):
    return render(request, 'app/index.html' )