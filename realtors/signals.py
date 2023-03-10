# code
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Realtor

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        realtor = Realtor(user = instance,email = instance.email,top_seller = False)
        realtor.save()
  
