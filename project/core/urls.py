from django.urls import path
from .views import Index, add_cart, cart, Address_order, Detail, remove_cart

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name = 'home'),
    path('add/<int:pk>', add_cart, name = 'add_cart'),
    path('cart', cart, name = 'cart'),
    path('Address_order', Address_order, name = 'address_order'),
    path('detail/<int:pk>', Detail.as_view(),  name='detail'),
    path('remove/<int:pk>', remove_cart, name='remove')

]