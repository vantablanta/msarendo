from django.urls import path
from .import views


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

]


        