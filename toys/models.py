from contextlib import nullcontext

from django.db import models

# Create your models here.
class addres(models.Model):
    street = models.CharField(max_length=25)
    city = models.CharField(max_length=25,null=True,blank=True)
    zip_code = models.CharField(max_length=25,null=True,blank=True)
    country = models.CharField(max_length=25,null=True,blank=True)



class user(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25,null=True,blank=True)
    email = models.EmailField(max_length=25,null=True,blank=True)
    phone = models.CharField(max_length=25,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.firstname


    Addres = models.OneToOneField(addres,on_delete=models.PROTECT,null=True,blank=True)
class tag(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(null=True,blank=True)

class toy(models.Model):
    name = models.CharField(max_length=25)
    User = models.ForeignKey(user,related_name='toys',on_delete=models.CASCADE,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    tags = models.ManyToManyField(tag, related_name='toys')
    created_at = models.TimeField(auto_now=True)
    upteted_at = models.TimeField(auto_now=True)

class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.CharField(max_length=1000, blank=True)
    admin_name = models.CharField(max_length=200)
    admin_email = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=9,decimal_places=2)
    email = models.EmailField(unique=True, null=True)



