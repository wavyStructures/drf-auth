from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    net_worth = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.name


class ManufacturerUser(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, blank=True, null=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.manufacturer.name})"


class Product(models.Model):    #inheriting from models.Model giving access to all methods and attributes for interacting with the database
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.name
