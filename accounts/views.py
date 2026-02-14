from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('dziala')
    #return render(request, 'accounts/home.html')
