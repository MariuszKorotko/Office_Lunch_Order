from django.contrib.auth.mixins	import LoginRequiredMixin
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from .forms import Order, NewOrderForm, OrderedDinnersForm, CloseOrderForm

class OrdersView(LoginRequiredMixin, View):
    """GET display orders ordered by date"""
    def get(self, request):
        orders = Order.objects.order_by('add_date')
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
        """Default data for user nad order"""
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
        """Display all dinners to choose"""
        order = Order.objects.get(pk=id)
        ordered_dinners = order.ordereddinners_set.all()
        # initial CloseOrderForm using id from CloseOrderForm which is hidden
        form = CloseOrderForm(initial={'id': id})
        context = {
            "order": order,
            "ordered_dinners": ordered_dinners,
            "form": form
        }
        return render(request, "order_details.html", context)

class CloseOrderView(LoginRequiredMixin, View):
    def post(self, request):
        """Send data using POST and change value of ordered from Order's
        model"""
        form = CloseOrderForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data["id"]
            order = Order.objects.get(pk=id)
            order.ordered = True
            order.save()
        return HttpResponseRedirect('/orders/')
