from django.http import HttpResponse
from django.urls import path

from Erplite.views import home

urlpatterns = [
    path('', home),
   
]