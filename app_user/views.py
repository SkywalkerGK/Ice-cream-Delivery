from django.core.mail import EmailMessage
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app_user.forms import RegisterForm,UserProfileForm,ExtendedProfileForm
from django.contrib.auth import login
from app_user.models import CustomUser
from app_user.utils.activation_token_generator import activation_token_generator

from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding  import force_bytes



# Create your views here.

def register(request: HttpRequest):
    # POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Register User
            user: CustomUser = form.save(commit=False)
            user.is_active = False
            user.save()



            #login(request, user)

            # Build email body HTML
            context = {
                "protocol": request.scheme,
                "host": request.get_host(),
                "uidb64": urlsafe_base64_encode(force_bytes(user.id)),
                "token": activation_token_generator.make_token(user)
            }
            email_body = render_to_string("app_users/activate_email.html",context)
            
            
            # Send email
            email = EmailMessage(to=[user.email], 
                subject="Active account หน่อยครับ",
                body=email_body
            )
            email.send()

            # Redirect to thank you
            return HttpResponseRedirect(reverse("register_thankyou"))
    else:
        form = RegisterForm()    
        
    # GET    
    context = {"form" : form }
    return render(request, "app_users/register.html",context)

def register_thankyou(request: HttpRequest):
    return render(request, "app_users/register_thankyou.html")

def activate(request: HttpRequest, uidb64: str, token: str):
    title = 'Active Account เรียบร้อยแล้ว'
    description = "เข้าสู่ระบบได้เลย"


    # Decode user id
    id = urlsafe_base64_decode(uidb64).decode()

    try:
        user: CustomUser = CustomUser.objects.get(id=id)
        if not activation_token_generator.check_token(user, token):
            raise Exception("Check token false")
        user.is_active = True
        user.save()
    except:
        print('Activate ไม่ผ่าน')
        title = 'Active Account ไม่ได้'
        description = "ลิ้งค์อาจถูกใช้ไปแล้ว หรือหมดอายุ"

    context = {"title":title , 'description':description}
    return render(request,"app_users/activate.html",context)

@login_required #ตรวจสอบการ Log in ถ้าไม่มีเข้า Dashboard ไม่ได้
def dashboard(request: HttpRequest):
    return render(request, "app_users/dashboard.html")

@login_required
def profile(request: HttpRequest):
    user = request.user
    #POST
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user) #Saveแบบ USER (โหลดข้อมูลของข้อมูลนั้นเข้ามาใน Modelform)
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
        form = UserProfileForm(instance=user)
        try:
            extended_form = ExtendedProfileForm(instance=user.profile)
        except:
            extended_form = ExtendedProfileForm()
     
    #GET
    context = {
        "form": form,
        "extended_form": extended_form
    }
    return render(request, "app_users/profile.html" , context)
    