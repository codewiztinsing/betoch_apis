from django.contrib import admin
from .models import Order,OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "created_at",
        # "paid_amount",
        
        )

    list_display_links = ('id','email')



