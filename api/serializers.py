from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "nome_vendor", "email", "status"]

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "city", "state", "vendor_id"]