from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation, Room
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your views here.

@login_required
def rooms_home(request):

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.created_by = request.user
            try:
                reservation.full_clean()
                reservation.save()
                messages.success(request, "Zarezerwowano ✅")
                return redirect("rooms:rooms_home")
            except ValidationError as e:
                for msg in e.messages:
                    messages.error(request, msg)
        else:
            messages.error(request, "Popraw błędy w formularzu.")
    else:
        form = ReservationForm()

    selected_room = request.GET.get("room", "")  # id sali jako string
    only_mine = request.GET.get("mine") == "1"  # checkbox

    reservations = Reservation.objects.filter(start__gte=timezone.now()).order_by("start")

    if selected_room:
        reservations = reservations.filter(room_id=selected_room)

    if only_mine:
        reservations = reservations.filter(created_by=request.user)

    rooms = Room.objects.order_by("name")

    return render(request, "rooms/home.html", {
        "form": form,
        "reservations": reservations,
        "rooms": rooms,
        "selected_room": selected_room,
        "only_mine": only_mine,
    })