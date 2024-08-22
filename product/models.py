from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import random
import string
from user.models import User


class Type(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='media/', null=True)
    
    class Meta:
        db_table = 'types'
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'brands'
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='media/', null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    real_price = models.IntegerField(validators=[MinValueValidator(0)])
    size = models.CharField(max_length=10, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.CharField(max_length=10, null=True)
    serial_number = models.CharField(max_length=10, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)
    about = models.TextField(null=True, max_length=1000, blank=True)
    rating_count = models.PositiveIntegerField(default=0)
    sale = models.BooleanField(default=False)
    sale_amount = models.TextField(null=True, max_length=1000, blank=True)
    like_count = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.serial_number:
            self.serial_number = self.generate_serial_number()
        super().save(*args, **kwargs)
    
    def generate_serial_number(self):
        length = 6
        while True:
            serial_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
            if not Product.objects.filter(serial_number=serial_number).exists():
                break
        return serial_number
    
    def update_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            total_rating = sum(rating.score for rating in ratings)
            self.average_rating = total_rating / ratings.count()
            self.rating_count = ratings.count()
            self.save()
            
    def update_like_count(self):
        self.like_count = self.likes.count()
        self.save()


class Rating(models.Model):
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])  # 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('product', 'user')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.update_rating()


class Like(models.Model):
    product = models.ForeignKey(Product, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')
    