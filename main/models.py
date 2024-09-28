from django.contrib.auth.models import User
from django.db import models
import uuid

class Sneakers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=2083)
    quantity = models.IntegerField() 


