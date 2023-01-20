from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Listing
from .serializers import ListingSerializer,ListingDetailSerializer
from rest_framework.routers import DefaultRouter


class ListingsView(ListAPIView):
	queryset = Listing.objects.filter(published = True)
	serializer_class = ListingSerializer
	# permission_classes = (permissions.AllowAny)
	pagination_class = None


class ListingViewSet(viewsets.ModelViewSet):

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
   

router = DefaultRouter()
router.register(r'', ListingViewSet,basename="listings")
# class ListingCreateView(APIView):

# 	def post(self,request,format = None):
# 		ls_data = ListingSerializer(data = self.request.data)
# 		if ls_data.is_valid():
# 			ls_data.save()
# 			return Response(ls_data.data,status.HTTP_200_OK)

# 		return Response({'message':"listing creation"},status.HTTP_400_BAD_REQUEST)



class ListingCreateView(CreateAPIView):
	queryset = Listing.objects.all()
	serializer_class = ListingSerializer
	
	







class ListingView(ListAPIView):
	queryset           = Listing.objects.filter(published = True)
	serializer_class   = ListingDetailSerializer
	# permission_classes = (permissions.AllowAny)
	lookup_field       = 'slug'



class SearchView(APIView):

	def post(self,request,format = None):
		
		permissions_classes = (permissions.AllowAny,)
		queryset = Listing.objects.filter(published = True)
		data   =  self.request.data

		# sale_type = data['sale_type']  
		# queryset = queryset.filter(sale_type__iexact = sale_type)

		home_type = data['home_type'] 
		city = data['city']  
		
		if not home_type and not city:
			queryset = Listing.objects.filter(published = True)

			
		if home_type:
			queryset = queryset.filter(home_type = home_type) 

		if home_type and city:
			queryset = queryset.filter(home_type = home_type).filter(city = city) 

		

		# city = data['city']  
		# queryset = queryset.filter(city__iexact = city)  

		serialize = ListingSerializer(queryset,many = True)
		return Response(serialize.data) 
		









class RelatedSearchView(APIView):

	def post(self,request,format = None):
		
		permissions_classes = (permissions.AllowAny,)
		queryset = Listing.objects.filter(published = True)
		data   =  self.request.data

		# sale_type = data['sale_type']  
		# queryset = queryset.filter(sale_type__iexact = sale_type)

		home_type = data['home_type'] 
		city = data['city']  
		price = data['price']
		q1 = Listing.objects.filter(home_type__contains = home_type)
		q2 = Listing.objects.filter(city__contains = city)
		q13 = Listing.objects.filter(price__l = price)


		

		# city = data['city']  
		# queryset = queryset.filter(city__iexact = city)  

		serialize = ListingSerializer(queryset,many = True)
		return Response(serialize.data) 
		





