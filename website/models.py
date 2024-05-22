from django.db import models

class Product(models.Model):
    title= models.CharField(max_length=200)
    id=models.IntegerField(primary_key=True)
    campany=models.CharField(max_length=200)

# Create your models here.
