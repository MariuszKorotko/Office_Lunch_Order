from .models import Order, OrderedDinners
from django.forms import ModelForm

class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'ordering_user']

class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['dinners']

class OrderedDinnersForm(ModelForm):
    class Meta:
        model = OrderedDinners
        fields = ['user', 'dinner','order']
