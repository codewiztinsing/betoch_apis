from django.contrib import admin
from .models import ServiceFee


@admin.register(ServiceFee)
class ServiceFeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "realtor",
        "fee",
        
        )

    list_display_links = ('realtor',)



