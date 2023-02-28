from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
          FavoriteViewSet,
          FavoriteListView,FavoriteListView
            
            )


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', FavoriteViewSet,basename="favs")


urlpatterns = [
  path('myfav/',FavoriteListView.as_view(),name = 'myfav')
    
]

urlpatterns += router.urls

