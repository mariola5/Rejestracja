from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.

@login_required
def rooms_home(request):
    return render(request, "rooms/home.html")