from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=256)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=64, validators=[phone_regex],
                                    blank=True)

    def __str__(self):
        return self.name

class Dinner(models.Model):
    name = models.CharField(max_length=128)
    restaurant = models.ForeignKey(Restaurant, default=1)
    description = models.TextField()
    price = models.FloatField()

class Order(models.Model):
    name = models.CharField(max_length=256, default="Zamawiamy obiad na 13.00!")
    ordering_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    dinners = models.ManyToManyField(Dinner)
    ordered = models.BooleanField()
    date_add = models.DateTimeField(default=datetime.now(), blank=True)

class OrderedDinners(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    dinner = models.ForeignKey(Dinner)
    order = models.ForeignKey(Order)