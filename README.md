# Office_Lunch_Order
This app help you to order lunch in your company simply way!

### Models:
- Restaurant (phone_regex field).
- Dinner (relationship many-to-one with Restaurant)
- Order (relationship many-to-many through OrderedDinners model)
- OrderedDinners (relationship many-to-one with User, Dinner, Order models)

### Views:

**- OrdersView display last 8 orders:**
=======================================
```
class OrdersView(LoginRequiredMixin, generic.ListView):
    template_name = 'office_lunch_order/orders.html'

    # Alternative solution viriable orders in orders.html instead order_list
    # context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.order_by('-add_date')[:8]
```

**- NewOrderView create new order using GET and POST method:

```
class NewOrderView(LoginRequiredMixin, View):
    def get(self, request):
        form = NewOrderForm()
        context = {
            "form": form
        }
        return render(request, "office_lunch_order/new_order.html", context)

    def post(self, request):
        form = NewOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('/officelunchorder/add_order/{}/'.format(order.id))
```

- AddOrderView add lunches into order:

```
class AddOrderView(LoginRequiredMixin, View):
    def get(self, request, id):
        """Default data for user and order"""
        form = OrderedDinnersForm(initial={'user': request.user,
                                           'order': id
                                           })
        context = {
            "form": form,
        }
        return render(request, "office_lunch_order/new_order.html", context)

    def post(self, request, id):
        form = OrderedDinnersForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('/officelunchorder/orders/')
```

- OrderDetailsView:

```
class OrderDetailsView(LoginRequiredMixin, View):
    def get(self, request, id):
        """Display all dinners to choose"""
        order = Order.objects.get(pk=id)
        ordered_dinners = order.ordereddinners_set.all()
        restaurants = Restaurant.objects.order_by('name')
        # initial CloseOrderForm using id from CloseOrderForm which is hidden
        form = CloseOrderForm(initial={'id': id})
        context = {
            "order": order,
            "ordered_dinners": ordered_dinners,
            "restaurants": restaurants,
            "form": form
        }
        return render(request, "office_lunch_order/order_details.html", context)
```

- CloseOrderView - can't join if order is closed:

```
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
        return HttpResponseRedirect('/officelunchorder/orders/')
```


