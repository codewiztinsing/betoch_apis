from .serializers import FavoriteSerializer
from rest_framework import viewsets
from .models import Favorite

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    pagination_class   = None
    

