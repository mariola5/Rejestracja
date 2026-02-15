from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation
# Create your views here.

@login_required
def rooms_home(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.created_by = request.user
            reservation.full_clean()
            reservation.save()
            return redirect("rooms:rooms_home")
    else:
        form = ReservationForm()

    reservations = Reservation.objects.order_by("start")

    return render(request, "rooms/home.html", {"form": form, "reservations": reservations})