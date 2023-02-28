from django.shortcuts import render
from order.models import Order
import json
import random
    # obj = {
    #     "process": "Express",
    #     "successUrl": "http://127.0.0.1:8000//success",
    #     "ipnUrl": "http://127.0.0.1:8000/ipn",
    #     "cancelUrl": "http://127.0.0.1:8000/cancel",
    #     "merchantId": "SB2114",
    #     # "merchantOrderId": "l710.0",
    #     "expiresAfter": 24,
    #     "items":[
    #         {
    #            "itemId": random.randint(1,10000),
    #             "itemName": "House transctions ",
    #             "unitPrice": 15,
    #             "quantity": 1,
    #             "discount": 0.0,
    #             "handlingFee": 0.0,
    #             "deliveryFee": 0.0,
    #             "tax1": 0.0,
    #             "tax2": 0.0
    #         }
    #     ],
     
        
    # }

def payment_with_express(request):
 
    obj = {

                "process":"Express",

                "successUrl":"http://127.0.0.1:8000/success/",

                "ipnUrl":"http://127.0.0.1:8000/cancel/",

                "merchantId":"SB2114",

                "merchantOrderId":"SB2114",

                "expiresAfter":24,

                "items":[

                    {

                        "itemId":"sku-01",

                        "itemName":"sample item",

                        "unitPrice":230,

                        "quantity":1

                    }

                ],

                "totalItemsDeliveryFee":12.3,

                "totalItemsTax1":35.5

            }
    return  render(request,'payments/index.html',{'obj':obj,'order':{}})





def success(request):
    oi= request.GET.get('itemId')
    total = request.GET.get('TotalAmount')
    moi = request.GET.get('MerchantOrderId')
    ti = request.GET.get('TransactionId')
    status = request.GET.get('Status')
    url = 'https://testapi.yenepay.com/api/verify/pdt/'
    datax = {
        "requestType": "PDT",
        "pdtToken": "Q1woj27RY1EBsm",
        "transactionId": ti,
        "merchantOrderId": moi
    }
    x = requests.post(url, datax)
    if x.status_code == 200:
        print("It's Paid")
        order = Order.objects.get(id = oi)
        order.status = "PAID"
        order.save()
    else:
        print('Invalid payment process')
    return render(request, 'pay/success.html', {'total': total, 'status': status,})




def cancel(request):
    return render(request, 'pay/cancel.html')

def ipn(request):
    return render(request, 'pay/ipn.html')