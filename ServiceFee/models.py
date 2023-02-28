from django.db import models
from listings.models import Listing
from realtors.models import Realtor

# Create your models here.

class ServiceFee(models.Model):
	listing = models.ForeignKey(Listing,on_delete = models.CASCADE)
	realtor = models.ForeignKey(Realtor,on_delete = models.CASCADE)
	fee   = models.IntegerField(default = 100)

	def __str__(self):
		return f"{self.realtor.name} service charge ${self.fee}"

