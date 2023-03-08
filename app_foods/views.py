from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Food


# Create your views here.
def foods(request):
    all_foods = Food.objects.order_by('-is_premium')
    context = {'foods':all_foods} #ส่งไปอ่านค่าในฟังชัน
    return render(request,'app_foods/foods.html',context)

def food(request,food_id):
    one_food = None
    try:
        one_food = Food.objects.get(id=food_id)
    except:
        print("หาไม่เจอ หรือเธอไม่มี")
    
    context = { 'food' : one_food ,'food_id': food_id }
    return render(request,'app_foods/food.html', context)

