from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
	list_display = ('email',)
	list_display_links = ('email',)
	

admin.site.register(Subscriber,SubscriberAdmin)
