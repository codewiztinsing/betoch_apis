from django.db import models
from datetime import datetime

class Realtor(models.Model):
	user        = models.ForeignKey('accounts.UserAccount',null = True,on_delete = models.CASCADE)
	name        = models.CharField(max_length = 25)
	photo       = models.ImageField(upload_to= 'photos/%Y/%m/%d')
	description = models.TextField()
	email       = models.EmailField(unique = True)
	phone       = models.CharField(max_length = 10)
	top_seller  = models.BooleanField(default = False)
	balance     = models.FloatField(default = 100.00)
	Account_number = models.IntegerField(null = True)
	created_at  = models.DateTimeField(default = datetime.now)


	def __str__(self):
		return self.email
