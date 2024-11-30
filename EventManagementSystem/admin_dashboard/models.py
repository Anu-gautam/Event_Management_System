from django.db import models
from vendors.models import Vendor

class Membership(models.Model):
    title = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.IntegerField()

class Transaction(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)