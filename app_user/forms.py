from django.contrib.auth.forms import UserCreationForm
from django import forms
from app_user.models import Profile, CustomUser

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields+("email",)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name","last_name")

class ExtendedProfileForm(forms.ModelForm):
    prefix = "extended"
    class Meta:
        model = Profile
        fields = ("address","phone") 
        locals = {
            "address": "ที่อยู่",
            "phone": "เบอร์โทรศัพท์"
        }
        widgets = {
            "address": forms.Textarea(attrs={"rows" : 3})
        }
