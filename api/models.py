from django.db import models

# Create your models here.

class Vendor(models.Model):
    nome_vendor = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    status = models.BooleanField(null=False, default=1)

class City(models.Model):
    city = models.CharField(null=False, max_length=50)
    state = models.CharField(null=False, max_length=2)
    vendor = models.OneToOneField(Vendor, on_delete=models.SET_NULL, null=True)