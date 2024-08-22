from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field import modelfields
from django.utils.crypto import get_random_string

class Region(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'regions'
        
    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'cities'
        
    def __str__(self):
        return self.name
        
        
class User(AbstractUser):
    phone = modelfields.PhoneNumberField(unique=True, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey('product.Product', on_delete=models.SET('deleted'))
    added = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)
    address = models.TextField(null=True, max_length=1000)
    serial_number = models.CharField(max_length=20, blank=True, unique=True)

    def generate_serial_number(self):
        self.serial_number = get_random_string(length=20)

    class Meta:
        db_table = 'orders'
    
    def __str__(self):
        return str(self.user)
