
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('markets.urls')),
    path('toys/',include('toys.urls'),name='toys'),
    path('admin/', admin.site.urls),
]
