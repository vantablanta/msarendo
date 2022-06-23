from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('login/', views.login_user, name='login'),
path('logout/', views.logout_user, name='logout'),
path('register/', views.register_user, name='register'),


path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),

path('jobs/', views.jobs, name='jobs'),
path('job/<str:name>', views.job_details, name='job'),
path('employer/<str:name>', views.employer_details, name='employer'),
path('applicants/<str:pk>', views.applicants, name='applicants'),

path('post-jobs/', views.post_job, name='post'),
path('close/<str:name>', views.delete_job, name='close'),


path('candidates/', views.candidates, name='candidates'),
path('candidate/<str:name>', views.candidate_details, name='candidate'),
path('profile/', views.profile, name='profile'),
path('edit-profile/', views.edit_profile, name='edit-profile'),
path('apply/<str:pk>', views.apply_job, name='apply'),

path('contract/<str:name>', views.contract, name='contract'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


        