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

### Templates:


