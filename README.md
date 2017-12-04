# Office_Lunch_Order
This app help you to order lunch in your company simply way!

### Models:

**- Restaurant:**
```python
class Restaurant(models.Model):
    name = models.CharField(max_length=256)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="""Phone number must be entered in
                                            the format: '+999999999'.
                                            Up to 15 digits allowed.""")
    phone_number = models.CharField(max_length=64,
                                    validators=[phone_regex],
                                    blank=True)

    def __str__(self):
        return self.name
```

**- Dinner:**
```python
class Dinner(models.Model):
    name = models.CharField(max_length=128)
    restaurant = models.ForeignKey(Restaurant, default=1)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        """Display menu with name of restaurant, dinner, and price"""
        result = "{} - {} ({} PLN)".format(self.restaurant.name,
                                           self.name,
                                           self.price)
        return result
```
**- Order:**
```python
class Order(models.Model):
    name = models.CharField(max_length=256, default="Zamawiamy obiad na 13.00!")
    ordering_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    dinners = models.ManyToManyField(Dinner, through='OrderedDinners')
    ordered = models.BooleanField(default=False)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

**- OrderedDinners:**
```python
class OrderedDinners(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    dinner = models.ForeignKey(Dinner)
    order = models.ForeignKey(Order)
```

### Views:

**- OrdersView display last 8 orders:**

```python
class OrdersView(LoginRequiredMixin, generic.ListView):
    template_name = 'office_lunch_order/orders.html'

    # Alternative solution for variable orders in orders.html instead order_list
    # context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.order_by('-add_date')[:8]
```

**- NewOrderView create new order using GET and POST method:**

```python
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

**- AddOrderView add lunches into order:**

```python
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

**- OrderDetailsView:**

```python
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

**- CloseOrderView - can't join if order is closed:**

```python
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


