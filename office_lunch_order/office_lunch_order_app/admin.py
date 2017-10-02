from django.contrib import admin
from .models import Restaurant, Dinner, Order


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Restaurant's name", {'fields': ['name']}),
        ("Phone's number:", {'fields': ['phone_number']}),
    ]

@admin.register(Dinner)
class DinnerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ("Restaurant:", {'fields':  ["restaurant"]}),
        ('Description:', {'fields': ["description"]}),
    ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "add_date", "ordering_user", "ordered")
