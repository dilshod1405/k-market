from django.urls import path, include
from .views import AdvertisementManageView, AdvertisementView
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register(r'manage', AdvertisementManageView)

urlpatterns = [
    path('', include(routers.urls)),
    path('all/', AdvertisementView.as_view(), name='advertisements'),
]
