from django.shortcuts import render, redirect
from .forms import Login, Register
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def account_logout(request):
    logout(request)
    return redirect('home:home')

def account_login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            login(request, user=user)
            return redirect('home:home')
    else: 
        form = Login()
    return render(request, 'login.html', {'form':form})

def register_account(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], password=cd['password'], email=cd['email'])
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home:home')
    else:
        form = Register()
    return render(request, 'register.html', {'form':form})