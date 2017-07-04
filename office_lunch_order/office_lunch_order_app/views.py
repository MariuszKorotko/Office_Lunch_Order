from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib.auth.mixins	import LoginRequiredMixin

class OrdersView(LoginRequiredMixin, View):
    def get(self, request):
        orders = Order.objects.order_by('date_add')
        context = { "orders": orders }
        return render(request, "orders.html", context)