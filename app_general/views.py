from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from app_foods.models import Food
from app_general.forms import SubscriptionForm
from .models import Subscription


# Create your views here.
def home(request):
    return render(request,'app_general/home.html')

def about(request):
    return render(request,'app_general/about.html')
    #return HttpResponse('เกี่ยวกับเรา')

def subscription(request):
    if request.method== 'POST':
        form = SubscriptionForm(request.POST) 
        if form.is_valid():
            data = form.cleaned_data
            new_sub = Subscription()
            new_sub.name = data['name']
            new_sub.email = data['email']
            new_sub.save()
            new_sub.food_set.set(data['food_set'])
            print(data)
            return HttpResponseRedirect(reverse('subscription_thankyou'))
    else:
        form = SubscriptionForm()
    context =  {'form': form}
    return render(request, 'app_general/subscription_form.html',context)

def subscription_thankyou(request):
    return render(request,'app_general/subscription_thankyou.html')
