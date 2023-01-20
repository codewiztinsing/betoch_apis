from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import views
from .models import Order,OrderItem
from .serializers import OrderSerializer,OrderItemSerializer
from rest_framework.views import APIView


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderViewCreate(APIView):
    # queryset = Order.objects.all()
    # serializer_class = OrderSerializer

    def post(self,request,format = None):
        data = self.request.data
        orders = OrderSerializer(data = data)
        if orders.is_valid():
            orders.save()
            return Response({'message':orders.data})

        return Response({"message":"created successfullly"})
   



class OrderItemViewSet(viewsets.ModelViewSet):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

      

 