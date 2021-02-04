from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView
from .forms import toyForm

from .models import *

# Create your views here.
class dashboard(View):
    def get(self, request):
        users = User.objects.only('firstname')
        toys = Toy.objects.all()
        return render(request,'toys/dashboard.html',{'users': users,'toys':toys})

class ToyListView(ListView):
    model = Toy
    template_name = "toys/toylistview.html"

class ToyCreateView(CreateView):
    template_name = 'toys/toycreateview.html'
    form_class = toyForm
    success_url = '/toys/'



