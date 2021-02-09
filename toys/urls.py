from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.dashboard.as_view(),name='dashboard'),
    path('toylistview/',views.ToyListView.as_view(),name='toylistview'),
    path('toycreateview/', views.ToyCreateView.as_view(), name='toycreateview'),
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('employees/',views.EmployeListView.as_view(),name='employees'),
    path('employecreate/',views.EmpCreateView.as_view(),name='employecreate'),
    path('<int:pk>/editemployee/', views.EditEmployee.as_view(), name='editemployee')

]