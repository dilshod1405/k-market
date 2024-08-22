from rest_framework import serializers
from .models import Product, Type, Brand, Rating, Like

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class ProductViewSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(many=True, read_only=True)
    added = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    type = TypeSerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'


class ProductEditSerializer(serializers.ModelSerializer):
    added = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    type = TypeSerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'type', 'real_price', 'serial_number',  'added', 'about', 'sale', 'sale_amount')
