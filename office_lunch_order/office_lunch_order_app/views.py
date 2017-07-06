# from django.contrib.auth.models import User
from django.contrib.auth.mixins	import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import *

class OrdersView(LoginRequiredMixin, View):
    def get(self, request):
        orders = Order.objects.order_by('date_add')
        context = { "orders": orders }
        return render(request, "orders.html", context)

class NewOrderView(LoginRequiredMixin, View):
    def get(self, request):
        form = NewOrderForm()
        context = {
            "form": form
        }
        return render(request, "new_order.html", context)

    def post(self, request):
        form = NewOrderForm(request.POST)

        if form.is_valid():
            order = form.save()
            return redirect('/add_order/{}'.format(order.id))

class AddOrderView(LoginRequiredMixin, View):

    def get(self, request, id):
        form = OrderedDinnersForm(initial={'user': request.user,
                                           'order': id})
        context = {
            "form": form
        }
        return render(request, "new_order.html", context)

    def post(self, request, id):
        form = OrderedDinnersForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('/orders/')

class OrderDetailsView(LoginRequiredMixin, View):
    def get(self, request, id):
        order = Order.objects.get(pk=id)
        context = { "order": order}
        return render(request, "order_details.html", context)