from django.shortcuts import render
from rest_framework import viewsets, generics
from . import serializers
from .models import Advertisement
from rest_framework.response import Response
from rest_framework.permissions import  IsAdminUser, AllowAny


# Advertisement manage view for admin panel
class AdvertisementManageView(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = serializers.AdvertisementSerializer
    permission_classes = [IsAdminUser]


# Advertisement view for user
class AdvertisementView(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = serializers.AdvertisementSerializer
    permission_classes = [AllowAny]
    