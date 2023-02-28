from .serializers import FavoriteSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Favorite
from listings.models import Listing
from listings.serializers import ListingSerializer
from realtors.models import Realtor

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    pagination_class   = None

class FavoriteListView(APIView):
    def post(self,request,format = None):
        data = []
        queryset = Favorite.objects.filter(realtor_email = self.request.data['email'])
        if queryset.exists():
            realtor = Realtor.objects.get(email = self.request.data['email'])
            data = Listing.objects.filter(realtor = realtor)
            seriaized_data = ListingSerializer(data,many = True)
        return Response(seriaized_data.data)
    

