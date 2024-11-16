from django.urls import path
from .views import index, add_cart, cart, Address_order
urlpatterns = [
    path('', index, name = 'home'),
    path('add/<int:pk>', add_cart, name = 'add_cart'),
    path('cart', cart, name = 'cart'),
    path('Address_order', Address_order, name = 'address_order'),
]