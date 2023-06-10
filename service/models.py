from django.db import models


# Create your models here.

class ServiceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    isActivated = models.BooleanField(default=False)


class ServiceAutorization(models.Model):
    id = models.AutoField(primary_key=True)


class ServiceForms(models.Model):
    id = models.AutoField(primary_key=True)
    serviceType = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    validation = models.CharField(max_length=1000)
    isActivated = models.BooleanField(default=False)


class ServiceFee(models.Model):
    id = models.AutoField(primary_key=True)
    minAmount = models.IntegerField()
    maxAmount = models.IntegerField()
    value = models.IntegerField()
    type = models.CharField(max_length=100)


class ServiceHistory(models.Model):
    id = models.AutoField(primary_key=True)


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    isActivated = models.BooleanField(default=False)



