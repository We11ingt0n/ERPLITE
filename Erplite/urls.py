from django.http import HttpResponse
from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home),
    path('formulario', views.formulario),
    path('', views.login)
    
   
]