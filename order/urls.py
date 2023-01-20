from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet,OrderItemViewSet,OrderViewCreate


# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'', OrderViewSet,basename="orders")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('create/', OrderViewCreate.as_view(),name = 'order-create')

]