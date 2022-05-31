import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'marks1':'56','marks2':'58','marks3':'76','marks4':'86'})

def add(request):
    return render(request,"results.html")    

def add_name(request):
    return render(request,"base.html")    