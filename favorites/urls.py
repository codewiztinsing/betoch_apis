from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
          FavoriteViewSet
            
            )


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', FavoriteViewSet,basename="favs")


urlpatterns = [
    
]

urlpatterns += router.urls

