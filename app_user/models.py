from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Profile(models.Model):
    address = models.TextField(default="")
    phone =  models.CharField(max_length=15 , default="")
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)#เชื่อมกับโมเดล USER ของ django
