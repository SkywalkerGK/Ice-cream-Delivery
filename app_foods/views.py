from django.http.response import HttpResponse
from django.shortcuts import render


all_foods = [
    {'id':1,'title':'Dark Choco Premium','price':499,'is_premium':True},
    {'id':2,'title':'Red Spicy','price':349,'is_premium':False},
    {'id':3,'title':'Blue Glacier','price':349,'is_premium':False},
]


# Create your views here.
def foods(request):
    context = {'foods':all_foods}
    return render(request,'app_foods/foods.html',context)

def food(request,food_id):
    return render(request,'app_foods/food.html', context={'food_id': food_id})

