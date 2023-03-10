from rest_framework import serializers
from .models import Listing



class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Listing
        fields = [
            'id',
            'realtor',
            'get_realtor_name',
            'get_realtor_email',
            'get_realtor_phone',
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
            'date_added'
            # 'Latitude_of_city',
            # 'Longitude_of_city'
            ]





class ListingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = fields = [
            'id',
            'title',
            'get_realtor_name',
            'get_realtor_email',
            'get_realtor_phone',
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
            'date_added'
            # 'Latitude_of_city',
            # 'Longitude_of_city'
            ]
        lookup_field = 'slug'