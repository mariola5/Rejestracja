from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rooms_home(request):
    return HttpResponse("Rooms home works!")