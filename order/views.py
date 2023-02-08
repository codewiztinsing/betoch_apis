from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import views
from .models import Order,OrderItem
from .serializers import OrderSerializer,OrderItemSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from rest_framework.views import APIView
from rest_framework.routers import DefaultRouter

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "email"
    pagination_class = None


router = DefaultRouter()
router.register(r'', OrderViewSet,basename="orders")


class OrderViewCreate(APIView):
    # queryset = Order.objects.all()
    # serializer_class = OrderSerializer

    def post(self,request,format = None):

        data = self.request.data
        orders = OrderSerializer(data = data,many = True)
        if orders.is_valid():
            orders.save()
            return Response({'message':orders.data})

        return Response({"message":"order not created"})

class OrderViewRetrieve(RetrieveAPIView):
    queryset           = Order.objects.all()
    serializer_class   = OrderSerializer
    pagination_class   = None
    lookup_field       = 'email'

   



class OrderItemViewSet(viewsets.ModelViewSet):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

      

 