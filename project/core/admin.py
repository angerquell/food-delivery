from django.contrib import admin
from .models import * 

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Order_address)
admin.site.register(Cart)