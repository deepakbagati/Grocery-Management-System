from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class category(models.Model):
    category_img = models.FileField(upload_to="category_images/",max_length=250,null=True,default=None)
    category_title = models.CharField(max_length=50)

class Grocery(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_img = models.FileField(upload_to="product_images/", max_length=250, null=True, default=None)
    product_title = models.CharField(max_length=50)
    product_price = models.FloatField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
