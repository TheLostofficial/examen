from django.contrib import admin
from .models import Order, Product, PickupPoint
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(PickupPoint)

admin.site.unregister(Group)
