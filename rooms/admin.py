from django.contrib import admin
from rooms.models import Room, Reservation
# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'location', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'location')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('title', 'room', 'start', 'end', 'created_by')
    list_filter = ('room',)
    search_fields = ('title', 'room__name', 'created_by__username')