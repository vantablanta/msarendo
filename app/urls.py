from django.urls import path
from .import views


urlpatterns = [
path('login/', views.login_user, name='login'),
path('register/', views.register_user, name='register'),


path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('jobs/', views.jobs, name='jobs'),

]


        