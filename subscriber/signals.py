from django.db.models.signals import post_save, pre_delete
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from realtors.models import Realtor
from listings.models import Listing
from subscriber.models import Subscriber
from ServiceFee.models import ServiceFee

@receiver(post_save, sender=Listing)
def create_profile(sender, instance, created, **kwargs):
    if instance.published:
        fee = ServiceFee.objects.create(listing = instance,realtor = instance.realtor,fee = float(instance.price) * 0.2)
        fee.save()
        city = instance.city
        subs = Subscriber.objects.filter(city__contains = city)
        emails = []
        for sub in subs:
            if sub not in emails:
                emails.append(sub.email)
        send_mail('new house is posted near to you',f"house with ",'solomonboloshe11x@gmail.com',['aleludago@gmail.com'],fail_silently=False)



  