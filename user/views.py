from django.shortcuts import render
from .models import User, Order
from rest_framework import generics, status
from . import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken
from .permissions import IsOwner



# View all users for admin panel
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UsersListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# View user profile by id with detail information for admin panel
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UsersListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        user_serializer = serializers.UsersListSerializer(user)
        orders = Order.objects.filter(user=user)
        order_serializer = serializers.OrderSerializer(orders, many=True)
        
        return Response({
            'user': user_serializer.data,
            'orders': order_serializer.data
        })


# Create new user
class UserCreateView(generics.CreateAPIView):
    serializer_class = serializers.UserCreateSerializer
    permission_classes = [AllowAny]


# User login view
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # Initialize the serializer with the request data
        serializer = serializers.UserLoginSerializer(data=request.data)
        
        # Validate the serializer
        if serializer.is_valid():
            # Retrieve the validated user
            user = serializer.validated_data['user']
            
            # Create JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            # Return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User logout view
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserLogoutSerializer(data=request.data)
        if serializer.is_valid():
            refresh_token = serializer.validated_data.get('refresh')
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response(status=status.HTTP_205_RESET_CONTENT)
            except InvalidToken:
                return Response({'detail': 'Token is invalid or expired.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User manage profile
class UserEditView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserEditSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        # Ensure the object retrieved is the current user's profile
        return self.request.user
    
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        user_serializer = serializers.UsersListSerializer(user)
        return Response(user_serializer.data)