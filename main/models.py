from django.db import models

class Barang(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()