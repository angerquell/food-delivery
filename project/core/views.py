from django.shortcuts import render, redirect
from .models import Food, Cart, Order_address, Order, OrderItem
from .forms import AddressForm
from django.db.models import F
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


class Detail(DetailView):
    model = Food
    template_name = 'detail.html'
    context_object_name = 'food'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            count_quantity = Cart.objects.filter(user=self.request.user).aggregate(Sum('quantity'))
            context['cart_item_count'] = count_quantity['quantity__sum']
        else:
            context['cart_item_count'] = 0
        return context

class Index(ListView):
    model = Food
    context_object_name = 'foods'
    template_name = 'index.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            count_quantity = Cart.objects.filter(user=self.request.user).aggregate(Sum('quantity')) 
            context['cart_item_count'] = count_quantity['quantity__sum']
        else:
            context['cart_item_count'] = 0
        return context

@login_required
def cart(request):
    cart = Cart.objects.filter(user = request.user)

    total_price = sum([i.price for i in cart])
    return render(request, 'cart.html', {"carts":cart, 'total_price':total_price})

@login_required
def add_cart(request, pk):
    food = Food.objects.get(pk=pk)
    cart, created = Cart.objects.get_or_create(user = request.user, item = food)
    if created == False:
        cart.quantity = F('quantity') + 1  
    else:
        cart.quantity = 1
    cart.save()
    return redirect('home:home')

def remove_cart(request, pk):
    food = Food.objects.get(pk=pk)
    cart= Cart.objects.get(user = request.user, item = food)
    cart.delete()
    return redirect('home:cart')

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
            if not cart.exists():
                    return redirect('home:cart')  
            
            for i in cart:
                OrderItem.objects.create(
                    order = order,
                    food = i.item,
                    quantity = i.quantity
                )    
            cart.delete()
            return redirect('home:home')
    else:
        form = AddressForm()
    
    return render(request, 'Address_order.html', {'form':form})
