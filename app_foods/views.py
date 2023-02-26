from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render


all_foods = [
    {
    
    'id':1,'title':'Dark Choco Premium','price':4990,'is_premium':True,'promotion_end_at':datetime(2022,2,28)

     },
    {'id':2,'title':'Red Spicy','price':3490,'is_premium':False,'promotion_end_at':datetime(2022,2,15)
     
     },
    {
    'id':3,'title':'Blue Glacier','price':3490,'is_premium':False,'promotion_end_at':datetime(2022,2,15)
    
    },
]


# Create your views here.
def foods(request):
    context = {'foods':all_foods} #ส่งไปอ่านค่าในฟังชัน
    return render(request,'app_foods/foods.html',context)

def food(request,food_id):
    one_food = None
    try:
        one_food =[f for f in all_foods if f['id'] == food_id][0]
        
    except IndexError:
        print('ไม้่มีเธอ ไม่มีเธอ')
    
    context = { 'food' : one_food ,'food_id': food_id }
    return render(request,'app_foods/food.html', context)

