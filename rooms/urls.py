from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("", views.rooms_home, name="rooms_home"),  # /rooms/
    path("reservation/<int:pk>/delete/", views.reservation_delete, name="reservation_delete"),
]