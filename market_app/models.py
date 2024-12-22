from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.name
