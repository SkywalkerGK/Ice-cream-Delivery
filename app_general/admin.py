from django.contrib import admin
from .models import Subscription

# Register your models here.
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['name','email','status','registered_at']
    search_fields = ['name','email']
    list_filter = ['status']

admin.site.register(Subscription,SubscriptionAdmin)