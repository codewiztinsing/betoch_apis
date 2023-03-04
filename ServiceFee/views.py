from rest_framework import viewsets
from rest_framework.views import APIView
from .models import ServiceFee
from .serializers import ServiceFeeSerializers
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from realtors.models import Realtor
from ServiceFee.models import ServiceFee

class ServiceViewSet(viewsets.ModelViewSet):

    queryset = ServiceFee.objects.all()
    serializer_class = ServiceFeeSerializers
    lookup_field = 'pk'
    pagination_class = None


class PayServiceView(APIView):

	def post(self,request,format = None):
		realtor = 0

		data = self.request.data

		realtor = data['realtor']

		print(type(data['realtor']))
		realtor = Realtor.objects.get(pk = data['realtor'])
		old_price = realtor.balance
		new_price = old_price - 45
		realtor.balance = new_price
		realtor.save()
		ServiceFee.objects.create(realtor = realtor,fee = 45)

		return Response({"payment succed"})


router = DefaultRouter()
router.register(r'', ServiceViewSet,basename="servicefee")