from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def dashboard(request):
    users = user.objects.only('firtname')
    toys = toy.objects.all()
    return render(request,'toys/dashboard.html',{'users': users,'toys':toys})
