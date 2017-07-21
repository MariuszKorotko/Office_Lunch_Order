# Office_Lunch_Order
This app help you to order lunch in your company simply way!

### Models:
- Restaurant (phone_regex field).
- Dinner (relationship many-to-one with Restaurant)
- Order (relationship many-to-many through OrderedDinners model)
- OrderedDinners (relationship many-to-one with User, Dinner, Order models)

### Views:
- OrdersView display last 8 orders:
```
class OrdersView(LoginRequiredMixin, generic.ListView):
    template_name = 'office_lunch_order/orders.html'

    # Alternative solution viriable orders in orders.html instead order_list
    # context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.order_by('-add_date')[:8]
```
- NewOrderView create new order using GET and POST method:
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
### Templates:


