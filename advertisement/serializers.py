from rest_framework import serializers
from .models import Advertisement

# Advertisement Serializer
class AdvertisementSerializer(serializers.ModelSerializer):
    added = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = Advertisement
        fields = '__all__'
