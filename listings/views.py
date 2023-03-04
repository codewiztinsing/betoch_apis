from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Listing
from realtors.models import Realtor
from .serializers import ListingSerializer,ListingDetailSerializer
from rest_framework.routers import DefaultRouter
from django.shortcuts import render,redirect
from django.contrib.postgres.search import (
	SearchVector,
	SearchQuery, 
	SearchRank,
	TrigramSimilarity
	)


class ListingsView(ListAPIView):
	queryset = Listing.objects.filter(published = True)
	serializer_class = ListingSerializer
	pagination_class = None



class MyListingsView(APIView):
	def get(self,request,format = None):
		realtor_email = self.request.GET['email']
		queryset = Listing.objects.filter(realtor__email=realtor_email)
		print(queryset)
		serialized_data = ListingSerializer(queryset,many = True)
		return Response(serialized_data.data)




class ListingViewSet(viewsets.ModelViewSet):

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    pagination_class = None
   

router = DefaultRouter()
router.register(r'', ListingViewSet,basename="listings")


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
		

class FullTextSearch(APIView):
	def post(self,request,format = None):
		
		permissions_classes = (permissions.AllowAny,)
		data   =  self.request.data
		keyword = data['keyword']
		search_query = SearchQuery(keyword)



		# queryset = Listing.objects.annotate(
		# similarity=TrigramSimilarity('home_type', search_query),
		# ).filter(similarity__gt=0.1).order_by('-similarity')

		search_vector = SearchVector('title',weight="A") \
								+ SearchVector('home_type',weight="B") \
								+ SearchVector('sale_type',weight="B")\
								+ SearchVector('price',weight="A")\
								+ SearchVector('bed_rooms',weight="A")\
								+ SearchVector('bath_rooms',weight="A")

	

		queryset = Listing.objects.annotate(
				search=search_vector,
				rank=SearchRank(search_vector, search_query)
				).filter(search=search_query).filter(published = True).order_by('-rank')
		

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
		q13 = Listing.objects.filter(price__lt = price)

		serialize = ListingSerializer(queryset,many = True)
		return Response(serialize.data)



class AddandRetrieveFavoriteView(APIView):

	def post(self,request,format = None):
		return Response({"message":"add to favorite"})  

	def list(self,request,format = None):
		return Response({"message":"list of favorites"}) 

	def delete(self,request,format = None):
		return Response({"message":"remove from favorite"}) 
		



class MYListing(APIView):

	def post(self,request,format = None):
		permissions_classes = (permissions.AllowAny,)
		queryset = Listing.objects.all()
		data   =  self.request.data
		realtor = Realtor.objects.get(email = data['email'])
		queryset = queryset.filter(realtor = realtor)
		serialize = ListingDetailSerializer(queryset,many = True)
		return Response(serialize.data)

	


def useraddlisting(request):
	from .forms import ListingForm
	form = ListingForm()

	if request.method == "POST":
		form = ListingForm(request.POST or None,request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect("listing:mylisting")
			

	return render(request,'listing/index.html',{'form':form})






def mylistings(request):
	print(request.GET)
	realtor = Realtor.objects.get(email = "aleludago@gmail.com")
	listings = Listing.objects.all().filter(realtor = 11)
	for listing in listings:
		print(listing.image.url)
	return render(request,"listing/mylistings.html",{"listings":listings})






 