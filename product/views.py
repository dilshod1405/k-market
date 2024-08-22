from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .models import Type, Brand, Product, Rating, Like
from . import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from .utils import generate_product_pdf


# View all types of products
class TypesView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = serializers.TypeSerializer
    permission_classes = [AllowAny]


# Type manage view
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = serializers.TypeSerializer
    permission_classes = [IsAuthenticated]


# View all brands
class BrandsView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer


# View product by id with detail information
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductViewSerializer


# View all products
class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductViewSerializer


# Add, edit and delete product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductEditSerializer
    permission_classes = [IsAuthenticated]
    

class ProductPdfView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductViewSerializer

    def get(self, request, *args, **kwargs):
        product_id = self.kwargs.get('pk')
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return HttpResponse(status=404)

        pdf_buffer = generate_product_pdf(product)
        
        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="product_{product_id}.pdf"'
        return response