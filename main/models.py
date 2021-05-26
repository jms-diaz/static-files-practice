from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField()
    price=models.IntegerField()
    images=models.ImageField(upload_to='images')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    