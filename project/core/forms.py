from django import forms
from .models import Order_address

class AddressForm(forms.Form):
    city = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100)
    number_home = forms.CharField(max_length=100)