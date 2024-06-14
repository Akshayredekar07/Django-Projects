from django.db import models

# Create your models here.
class Hydrabad_jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibilty=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.BigIntegerField()


class Bengluru_jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibilty=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.BigIntegerField()


class Pune_jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibilty=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.BigIntegerField()


