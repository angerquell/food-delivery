from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


class Food(models.Model):
    compound = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='food')
    description = models.TextField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Order_address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number_home = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Order_address, on_delete=models.CASCADE)
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.price = self.food.price * self.quantity
        super(OrderItem, self).save(*args, **kwargs)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        self.price = self.item.price * self.quantity
        super(Cart, self).save(*args, **kwargs)


    