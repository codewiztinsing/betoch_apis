from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

User = get_user_model()

class SignUpView(APIView):

	def post(self,request,format = None):
		data = self.request.data
		name = data['username']
		email = data['email']
		password = data['password']
		password2 = data['password2']
		is_realtor = data['is_realtor']

		if password == password2:
			if User.objects.filter(email = email).exists():
				return Response({'error':'Email Already Exists'})
			else:
				user = User.objects.create_user(email = email,name=name,password=password,is_realtor = is_realtor)
				user.save()
				return Response({'user_name':user.name,"user_email":user.email,"is_realtor":user.is_realtor})
		else:
			return Response({'message':'password does\'t match'})

	

class GetUserView(APIView):

	def post(self,request,format = None):
		payload = {}
		data = self.request.data
		email = data['email']
		user = User.objects.get(email = email)
		payload['realtor'] = user.is_realtor
		payload['name'] = user.name

		if not user:
			return Response({"message":"no user with given crendential"})
		return Response(payload)
