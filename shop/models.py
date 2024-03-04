from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(default="default.jpg",upload_to="product_pics")
    product_type = models.CharField(max_length=25,default="unknown")
    def __str__(self):
        return f'{ self.name }'

