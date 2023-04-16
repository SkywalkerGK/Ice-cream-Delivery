from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app_user.forms import RegisterForm,UserProfileForm,ExtendedProfileForm
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

@login_required #ตรวจสอบการ Log in ถ้าไม่มีเข้า Dashboard ไม่ได้
def dashboard(request: HttpRequest):
    return render(request, "app_users/dashboard.html")

@login_required
def profile(request: HttpRequest):
    user = request.user
    #POST
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user) #Saveแบบ USER
        is_new_profile = False #User มี Profile

        try:  #พยายามอัพเดตดูก่อน
            extended_form = ExtendedProfileForm(request.POST, instance=user.profile)
        except: #ถ้าไม่ได้จะสร้างโปรไฟล์อันใหม่
            extended_form = ExtendedProfileForm(request.POST)  
            is_new_profile = True   #User ไม่มี Profile

        if form.is_valid() and extended_form.is_valid():
            form.save()
            if is_new_profile: #สร้างใหม่
                profile = extended_form.save(commit=False)
                profile.user = user
                profile.save()
            else:  #เซฟเลย / อัพเดต
                extended_form.save()    


            return HttpResponseRedirect(reverse("profile"))
    else:
        form = UserProfileForm()
        extended_form = ExtendedProfileForm()

    #GET
    context = {
        "form": form,
        "extended_form": extended_form
    }
    return render(request, "app_users/profile.html" , context)
    