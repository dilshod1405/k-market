from django.urls import path, include
from .views import TypesView, BrandsView, ProductDetailView, ProductViewSet, ProductsView, ProductPdfView, TypeViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'type', TypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('types/', TypesView.as_view(), name='types'),
    path('brands/', BrandsView.as_view(), name='brands'),
    path('product/', ProductsView.as_view(), name='all-products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/pdf/', ProductPdfView.as_view(), name='product-pdf'),
]
