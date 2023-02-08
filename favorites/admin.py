from django.contrib import admin
from .models import Favorite


class FavoriteAdmin(admin.ModelAdmin):
	list_display = ('listing','realtor_email')
	list_display_links = ('listing',)
	

admin.site.register(Favorite,FavoriteAdmin)
