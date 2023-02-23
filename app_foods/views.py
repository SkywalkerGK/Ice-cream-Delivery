from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def foods(request):
    return HttpResponse('เมนู อร่อย ส่งบ่อย ส่งไว')

