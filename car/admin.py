from django.contrib import admin
from .models import Car_Model,Comment,Order
# Register your models here.

admin.site.register(Car_Model)
admin.site.register(Comment)
admin.site.register(Order)