from django.urls import path
from .views import DetailListView, ProductListView, CreateProductView

urlpatterns=[

    path('',ProductListView.as_view(), name='index'),
    path('<int:pk>/', DetailListView.as_view(), name='detail'),
    path('add/', CreateProductView.as_view(), name='add'),

]