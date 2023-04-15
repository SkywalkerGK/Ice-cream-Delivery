from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_user.forms import RegisterForm
from django.contrib.auth import login
# Create your views here.

def register(request: HttpRequest):
    # POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
    else:
        form = RegisterForm()    
        
    # GET    
    context = {"form" : form }
    return render(request, "app_users/register.html",context)
