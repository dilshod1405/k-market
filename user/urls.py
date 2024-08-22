from django.urls import path, include
from .views import UserListView, UserDetailView, UserCreateView, LoginView, LogoutView, UserEditView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # manager actions
    path('manager/users/', UserListView.as_view(), name='users-list-admin'),
    path('manager/user/<int:pk>/', UserDetailView.as_view(), name='users-detail-admin'),
    
    # user actions
    path('create/', UserCreateView.as_view(), name='new-user'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('<int:pk>/edit/', UserEditView.as_view(), name='user-edit'),
    
]