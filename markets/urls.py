from django.urls import path
from .views import ProductListView, MarketListView

urlpatterns=[
    path('',ProductListView.as_view(), name='index'),
    path('base/',MarketListView.as_view(), name='base'),
]