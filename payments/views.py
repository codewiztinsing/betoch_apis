from yenepay import Client, Item, Cart
from rest_framework.response import Response
from rest_framework.views import APIView
from order.models import Order 


class Payment(APIView):
	def post(self,request,format = None):

		print(self.request)

		return Response({"message":"debug"})

	