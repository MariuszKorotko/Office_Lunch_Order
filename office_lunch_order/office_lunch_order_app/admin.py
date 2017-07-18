from django.contrib import admin
from .models import Restaurant, Dinner, Order

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number")

@admin.register(Dinner)
class DinnerAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant", "description", "price")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "add_date", "ordering_user", "ordered")
