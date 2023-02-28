from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Subscriber
from .serializers import SubscriberSerializer

class Subscribe(APIView):
	def post(self,request,format = None):
		email = self.request.data.get('email')
		subscriber = Subscriber.objects.create(email = email)
		data  = SubscriberSerializer(subscriber,many = True)
		if data.is_valid():
			return Response(data.data)
		return Response({'message':"subscriber is not created"})

	def get(self,request,format = None):
		subscriber_list = Subscriber.objects.all()
		seriaized_data  = SubscriberSerializer(subscriber_list,many = True)
		return Response(seriaized_data.data)


	def delete(self,request,format = None):
		id = self.request.id
		subscriber = Subscriber.objects.get(id = id)
		subscriber.delete()
		seriaized_data  = SubscriberSerializer(subscriber_list,many = True)
		return Response(seriaized_data.data)
