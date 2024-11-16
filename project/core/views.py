from django.shortcuts import render, redirect
from .models import Food, Cart, Order_address, Order, OrderItem
from .forms import AddressForm
def index(request):
    foods = Food.objects.all()
    return render(request, 'index.html', {'foods':foods})

def cart(request):
    cart = Cart.objects.filter(user = request.user)
    return render(request, 'cart.html', {"carts":cart})

def add_cart(request, pk):
    food = Food.objects.get(pk=pk)
    cart, created = Cart.objects.get_or_create(user = request.user, item = food)
    if created == False:
        cart.quantity += 1 
    else:
        cart.quantity = 1
    cart.save()
    return redirect('home')


def Address_order(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            address = Order_address.objects.create(city =cd['city'],
                                         street = cd['street'],
                                         number_home = cd['number_home'],
                                         )
            order = Order.objects.create(user = request.user, address = address) 
            cart = Cart.objects.filter(user = request.user)
            for i in cart:
                OrderItem.objects.create(
                    order = order,
                    food = i.item,
                    quantity = i.quantity
                )    
            redirect('home')
    else:
        form = AddressForm()
    
    return render(request, 'Address_order.html', {'form':form})
