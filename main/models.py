from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    release_date = models.DateField()
    genre =  models.CharField(max_length=100)

