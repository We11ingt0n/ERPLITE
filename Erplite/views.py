from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    
   return  render(request,'Erplite\pages\home.html')

def formulario(request):
    
   return  render(request,'Erplite\pages\cad_nfunc.html')