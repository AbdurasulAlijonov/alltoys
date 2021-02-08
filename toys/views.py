from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView
from .forms import toyForm

from .models import Toy

# Create your views here.
class dashboard(View):
    def get(self, request):
        #users = User.objects.only('firstname')
        toys = Toy.objects.all()
        return render(request,'toys/dashboard.html',{'toys':toys})

class ToyListView(ListView):
    model = Toy
    template_name = "toys/toylistview.html"

class ToyCreateView(CreateView):
    template_name = 'toys/toycreateview.html'
    form_class = toyForm
    success_url = '/toys/'

def register(request):
    if request.method == 'GET':
        return render(request, 'toys/sign_up.html')
    if request.method =='POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                print('Username taken')
            else:

                user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,
                                 email=email,password=password)
                user.save()
                print('user created')
        return redirect('/')





