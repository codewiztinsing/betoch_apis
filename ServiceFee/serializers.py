from rest_framework import serializers
from .models import ServiceFee


class ServiceFeeSerializers(serializers.ModelSerializer):
	class Meta:
		model = ServiceFee
		fields = "__all__"