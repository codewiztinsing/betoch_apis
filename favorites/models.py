from django.db import models

class Favorite(models.Model):
	listing = models.ForeignKey('listings.Listing',on_delete = models.CASCADE,null = True)
	realtor_email = models.EmailField(null = True)


	def __str__(self):
		return f"{self.listing}"
