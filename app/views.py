from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PostJobForm, RegisterForm, UpdateProfileForm
from .models import AppliedJobs, Candidate, Profile, Job, Hired

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
    return render(request, 'app/index.html', ctx)


def about(request):
    return render(request, 'app/about.html')


def contact(request):
    return render(request, 'app/contact.html')


def user_role(request):
    user = request.user
    profile = Profile.objects.get(owner=user)
    ctx = {'profile': profile}
    return render(request, 'nav.html', ctx)


def jobs(request):
    jobs = Job.objects.all() 

    ctx = {'jobs': jobs}
    return render(request, 'app/jobs.html', ctx)


@login_required()
def post_job(request):
    profile = Profile.objects.get(owner = request.user)
    form = PostJobForm()
    if request.method == 'POST':
        form = PostJobForm(request.POST)
        if form.is_valid():
            new_job = form.save(commit = False)
            new_job.recruiter = profile
            new_job.save()
            return redirect('home')
    ctx= {'form': form}
    return render(request, 'app/post-jobs.html', ctx)


@login_required(login_url='login')
def delete_job(request, name):
    job = get_object_or_404(Job, title = name)
    page = 'delete job'
    if request.method == 'POST':
        job.delete()
        return redirect('profile')
    ctx = {'page': page, 'obj': job}
    return render(request, 'app/delete.html', ctx)


@login_required(login_url='login')
def job_details(request, name):
    job = Job.objects.get(title=name)
    ctx = {'job': job}
    return render(request, 'app/job-details.html', ctx)


@login_required(login_url='login')
def employer_details(request, name):
    employer = Job.objects.filter(recruiter__owner__username=name).first()
    ctx = {'employer': employer}
    return render(request, 'app/employer-details.html', ctx)


@login_required(login_url='login')
def candidates(request):
    candidates = Candidate.objects.all()
    ctx = {'candidates': candidates}
    return render(request, 'app/candidates.html', ctx)

@login_required(login_url='login')
def candidate_details(request, name):
    candidate = Candidate.objects.get(owner__owner__username=name)
    ctx = {'candidate': candidate}
    return render(request, 'app/candidate-details.html', ctx)

@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.get(owner=request.user)
    jobs_posted = Job.objects.filter(recruiter=profile)

    candidate = Candidate.objects.filter(owner=profile)

    applied_jobs = AppliedJobs.objects.filter(candidate__owner=profile)

    ctx = {'profile': profile, 'jobs_posted': jobs_posted,
        'candidate': candidate, 'applied_jobs': applied_jobs}
    return render(request, 'app/profile.html', ctx)

@login_required(login_url='login')
def edit_profile(request):
    profile = Profile.objects.get(owner=request.user)
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    ctx = {'profile': profile, 'form': form}
    return render(request, 'app/update-profile.html', ctx)


@login_required(login_url='login')
def applicants(request, pk):
    job = Job.objects.get(id=pk)
    ctx = {'job': job}
    return render(request, 'app/applicants.html', ctx)


@login_required(login_url='login')
def apply_job(request, pk):
    job = Job.objects.get(id=pk)
    user = request.user
    profile = Profile.objects.get(owner=user)
    applicant = Candidate.objects.get(owner=profile)
    job.applicants.add(applicant)

    new_candidate = AppliedJobs.objects.create(job = job, candidate = applicant)
    new_candidate.save()

    messages.success(request, f'You have successfully applied for the {job.title} Job. The client has been notified. All the best.')
    return redirect('jobs' )


@login_required(login_url='login')
def contract(request, name):
    candidate = Candidate.objects.get(owner__owner__username = name)
    job = Job.objects.get(applicants = candidate)
    if request.method == 'POST':
        new_match = Hired.objects.create(job = job, candidate=candidate)
        new_match.save()
    ctx = {'candidate' : candidate, 'job' : job}
    return render(request, 'app/contract.html', ctx)


