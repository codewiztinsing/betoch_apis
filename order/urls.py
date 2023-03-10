from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
            OrderViewSet,
        
            OrderViewCreate,
            router,
            OrderViewRetrieve,
            OrderListWithEmail
            
            )


# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'', OrderViewSet,basename="orders")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('myorders/',OrderListWithEmail.as_view(),name = 'order-email'),
    path('<email>/', OrderViewRetrieve.as_view(),name = 'order-retrieve'),
    path('create/', OrderViewCreate.as_view(),name = 'order-create'),
  

]

urlpatterns += router.urls