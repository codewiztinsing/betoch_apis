from django.db import models


class Subscriber(models.Model):
	email = models.EmailField(unique = False)
	city = models.CharField(max_length = 111,default = "shager")

	def __str__(self):
		return self.email
