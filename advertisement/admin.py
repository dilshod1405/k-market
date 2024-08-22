from django.contrib import admin
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'added', 'id')
    list_filter = ('added', )
    ordering = ('id', )