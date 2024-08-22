from rest_framework import serializers
from .models import User, City, Region, Order
from django.contrib.auth import authenticate

# Regions list
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')

# Cities list
class CitySerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    class Meta:
        model = City
        fields = ('id', 'name', 'region')

# Orders list
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'product', 'status')

# Users information for admin panel
class UsersListSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'phone', 'city')


# Create new user
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'phone', 'city')
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            phone=validated_data['phone'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            city=validated_data.get('city', '')
        )
        return user


# User login
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return {
            'user': user
        }
    

# User logout
class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)


# User edit
class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone', 'city')
        extra_kwargs = {
            'password': {'write_only': True}
        }
