from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='profile-home'),
    path('about/', views.about, name="profile-home-about"),
]