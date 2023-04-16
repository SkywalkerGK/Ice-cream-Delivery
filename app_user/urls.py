from django.urls import path , include
from . import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register', view=views.register, name="register"),
    path('dashboard', view=views.dashboard, name="dashboard"),
    path('profile', view=views.profile, name="profile"),
]