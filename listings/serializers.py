from rest_framework import serializers
from .models import Listing



class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Listing
        fields = [
            'id',
            'realtor',
            'get_realtor_name',
            'title',
            'city',
            'slug',
            'address',
            'state',
            'home_type',
            'sale_type',
            'bed_rooms',
            'bath_rooms',
            'sqrt',
            'oldPrice',
            'slug',
            'published',
            'description',
            'price',
            'get_image',
            'images',
            'image',
            'date_added',
            ]





class ListingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = fields = [
            'id',
            'title',
            'get_realtor_name',
            'city',
            'slug',
            'address',
            'state',
            'published',
            'home_type',
            'sale_type',
            'bed_rooms',
            'bath_rooms',
            'sqrt',
            'oldPrice',
            'slug',
            'published',
            'description',
            'price',
            'get_image',
            'images',
            'image',
            'date_added',
            ]
        lookup_field = 'slug'