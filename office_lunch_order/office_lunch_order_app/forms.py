from django.forms import ModelForm
from django import forms
from .models import Order, OrderedDinners

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
        fields = ['user', 'dinner', 'order']

class CloseOrderForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
