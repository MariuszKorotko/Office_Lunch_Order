from django.contrib import admin
from .models import *

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number")

@admin.register(Dinner)
class DinnerAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant", "description", "price")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "ordering_user", "ordered")