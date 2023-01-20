from .views import Payment
from django.urls import path

urlpatterns = [
	path('',Payment.as_view(),name = 'payment')

]