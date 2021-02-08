from contextlib import nullcontext
from django.db import models
from django.utils import timezone

from toys.enum import ToyTypeEnum


class Addres(models.Model):
    street = models.CharField(max_length=25)
    city = models.CharField(max_length=25,null=True,blank=True)
    zip_code = models.CharField(max_length=25,null=True,blank=True)
    country = models.CharField(max_length=25,null=True,blank=True)



class User(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25,null=True,blank=True)
    email = models.EmailField(max_length=25,null=True,blank=True)
    phone = models.CharField(max_length=25,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.firstname

    addres = models.OneToOneField(Addres,on_delete=models.PROTECT,null=True,blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

def logo_upload_path(inctance, filename):
    current_td = timezone.now
    #return f"toy-photos/{current_td.strftime('%Y_%m')}/{uuid.uuid4().hex}/{filename}"

class Toy(models.Model):
    name = models.CharField(max_length=25)
    user = models.ForeignKey(User,related_name='toys',on_delete=models.CASCADE,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    #type = models.CharField(max_length=ToyTypeEnum.max_length(), choices=ToyTypeEnum.get_value_tuples(), blank=True)
    photo = models.ImageField(upload_to='#', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='toys')
    created_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Toys'

class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.CharField(max_length=1000, blank=True)
    admin_name = models.CharField(max_length=200)
    admin_email = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=9,decimal_places=2)
    email = models.EmailField(unique=True, null=True)



