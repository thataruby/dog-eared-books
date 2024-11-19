import uuid 
from django.db import models
from django.contrib.auth.models import User

class BookEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    genre =  models.CharField(max_length=100)
    summary = models.TextField()

