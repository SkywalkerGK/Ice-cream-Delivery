from django.urls import path
from . import views

urlpatterns = [
    path('',views.foods, name='foods'), #foods/
    path('<int:food_id>',views.food, name='food') #foods/1 2 3


]