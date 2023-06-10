from django.db import models


# Create your models here.

class Client(models.Model):
    phone = models.CharField(max_length=100, unique=True)
    isVerified = models.BooleanField(default=False)
    isBlocked = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    isSuspended = models.BooleanField(default=False)


class Kyc(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    idType = models.CharField(max_length=100)
    idNumber = models.CharField(max_length=100)
    idImage = models.ImageField(upload_to='kyc/')
    isVerified = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    isSuspended = models.BooleanField(default=False)


