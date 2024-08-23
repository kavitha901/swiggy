from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def delivery(request):
    return HttpResponse('<h1><marquee>swiggy delivers the food afap</marquee></h1>')
