from rest_framework.generics import ListAPIView,RetrieveAPIView,ListCreateAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework import permissions,viewsets
from .models import Realtor
from .serializers import RealtorSerilizer
from rest_framework.views import APIView



class RealtorViewSet(viewsets.ModelViewSet):
    """
   
    """
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerilizer
   

class RealtorListView(ListAPIView):
	permission_classes = (permissions.AllowAny,)
	queryset = Realtor.objects.all()
	serializer_class = RealtorSerilizer
	pagination_class = None

	def list(self,request):
		print("from list method",self.queryset)



class RealtorUpdateView(APIView):


	def post(self,request,format = None):
		
		email = self.request.data['email']
		price = self.request.data['price']
		realtor = Realtor.objects.get(email = email)
		old_price = realtor.balance
		new_price = old_price + price
		realtor.balance = new_price
		realtor.save()
		print(realtor.balance)
		return Response({
			"realtor":"is update 1"
			})



class RealtorView(RetrieveAPIView):

	queryset = Realtor.objects.all()
	serializer_class = RealtorSerilizer
	lookup_field = 'email'
	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		# print(instance.realtor_orders.all())
		serializer = self.get_serializer(instance)
		return Response(serializer.data)


class RealtorViewWithPk(RetrieveAPIView):
	print("with pk is hit 1")
	queryset = Realtor.objects.all()
	serializer_class = RealtorSerilizer
	lookup_field = 'pk'
	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		# print(instance.realtor_orders.all())
		serializer = self.get_serializer(instance)
		return Response(serializer.data)

class RealtorCreateView(ListCreateAPIView):
	queryset = Realtor.objects.all()
	serializer_class = RealtorSerilizer
	
	
	


class TopSellerView(ListAPIView):
	permission_classes = (permissions.AllowAny,)
	queryset = Realtor.objects.filter(top_seller = True)
	serializer_class = RealtorSerilizer
	pagination_class = None
