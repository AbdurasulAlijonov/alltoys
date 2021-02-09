from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .forms import toyForm, EmployeeForm

from .models import Toy, Employee


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

class EmployeListView(ListView):
    model = Employee
    template_name = "toys/employees.html"


class EmpCreateView(CreateView):
    template_name = 'toys/employecreate.html'
    form_class = EmployeeForm

    def form_valid(self, form):
        self.object = form.save()
        return redirect('employees')

class EditEmployee(UpdateView):
    template_name = 'toys/editemployee.html'
    model = Employee
    queryset = Employee.objects.all()


    def get_object(self, queryset=Employee.objects.all()):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Employee,id=id_)

def register(request):

    if request.method =='POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,
                                 email=email,password=password)
                user.save()
        else:
            messages.info(request,'Password1 not exist to Password')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'toys/sign_up.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username or password wrong..')
            return redirect('login')
    else:
        return render(request,'toys/login.html')



