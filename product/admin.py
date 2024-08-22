from django.contrib import admin
from .models import Product, Type, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'real_price', 'serial_number', 'id')
    ordering = ('id',)
    list_filter = ('name', 'type')
    search_fields = ('name', )


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    ordering = ('id',)
    search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    ordering = ('id',)
    search_fields = ('name',)
    