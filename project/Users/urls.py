from django.urls import path
from .views import account_logout, account_login, register_account

app_name = "account" 

urlpatterns = [
    path('logout', account_logout, name='logout'),
    path('login', account_login, name='login'),
    path('register', register_account, name='register')
]