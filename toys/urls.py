from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.dashboard.as_view(),name='dashboard'),
    path('toylistview/',views.ToyListView.as_view(),name='toylistview'),
    path('toycreateview/', views.ToyCreateView.as_view(), name='toycreateview'),

]