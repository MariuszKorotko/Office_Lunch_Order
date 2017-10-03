from django.contrib import admin
from .models import Dinner, Order, Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Restaurant's name", {'fields': ['name']}),
        ("Phone's number:", {'fields': ['phone_number']}),
    ]
    search_fields = ['name']


@admin.register(Dinner)
class DinnerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('name', 'price')}),
        ("Restaurant:", {'fields':  ["restaurant"]}),
        ('Description:', {'fields': ["description"]}),
    ]
    search_fields = ['name']
    radio_fields = {"restaurant": admin.VERTICAL}
    list_filter = (
        ('restaurant', admin.RelatedOnlyFieldListFilter),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "add_date", "ordering_user", "ordered")
    list_filter = (
        ('ordered', admin.BooleanFieldListFilter),
    )
