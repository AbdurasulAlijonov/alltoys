#from msilib.schema import ListView

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from markets.models import Product, Market


class ProductListView(ListView):
    model = Product
    template_name = "markets/index.html"
    context_object_name = 'all'

    def get_queryset(self):
        queryset = {'products': Product.objects.all(),
                    'markets': Market.objects.all()}
        return queryset



class DetailListView(DetailView):
    model = Product
    template_name = 'markets/detail.html'
    #context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all'] ={ 'current_products':Product.objects.filter(market=self.kwargs.get(self.pk_url_kwarg)),
                          'markets': Market.objects.all(),
                          'products':Product.objects.all()}
        return context

class CreateProductView(CreateView):
    model = Product
    template_name = 'markets/add.html'
    fields = ('name','description','price','market')
    success_url = reverse_lazy('index')

