from django.db import models


# Create your models here.

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    serviceType = models.ForeignKey('service.ServiceType', on_delete=models.CASCADE)
    serviceForm = models.ForeignKey('service.ServiceForms', on_delete=models.CASCADE)
    serviceFee = models.ForeignKey('service.ServiceFee', on_delete=models.CASCADE)
    country = models.ForeignKey('service.Country', on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
