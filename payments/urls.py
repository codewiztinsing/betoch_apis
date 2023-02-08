from django.urls import path
from .views import  payment_with_express, success, cancel, ipn

urlpatterns = [
    path('', payment_with_express, name='express-payment'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    path('ipn/', ipn, name='ipn')
]