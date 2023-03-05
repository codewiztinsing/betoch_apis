from django.urls import path
from .views import  BuyerPayForRealtor

urlpatterns = [
    path('payforrealtor/',BuyerPayForRealtor.as_view(),name="BuyerPayForRealtor"),
   
]