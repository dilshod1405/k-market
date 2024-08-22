from django.contrib import admin
from .models import User
from .models import City
from .models import Region
from .models import Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "phone", 'city', 'id')
    ordering = ('id',)
    list_filter = ('city',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "region", 'id')
    ordering = ('id',)
    

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name", 'id')
    ordering = ('id',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "products", 'id')
    ordering = ('id',)
    list_filter = ('user', 'products', 'added')