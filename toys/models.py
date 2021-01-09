from django.db import models

# Create your models here.
class user(models.Model):
    firtname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    age = models.IntegerField()
