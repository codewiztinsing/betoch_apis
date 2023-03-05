from django.shortcuts import render
from order.models import Order
import json
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from realtors.models import Realtor
from listings.models import Listing
from order.models import Order

class BuyerPayForRealtor(APIView):
    def post(self,request,format = None):
        data = self.request.data

        price      = data['price']
        realtor_id = data['realtor']
        listing_id = data['listing']
        order_id   = data['id']

        realtor = Realtor.objects.get(pk = realtor_id)
        r_old_price = realtor.balance
        realtor.balance = float(r_old_price) + float(price)
        realtor.save()
        listing = Listing.objects.get(pk = listing_id)
        
        print("listing id ",listing.id)
        listing.delete()
        listing.save() 

        order = Order.objects.get(pk = order_id)
        order.delete()
        order.save()
        return Response({"pay for realtor":"successed"})


