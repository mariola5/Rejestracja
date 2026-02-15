from django.db import models
from django.db.models import Q, F
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200, unique=True)
    capacity = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    related_name='reservations')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.start or not self.end:
            return

        if self.start >= self.end:
            raise ValidationError("Koniec musi być po starcie.")

        if self.start < timezone.now():
            raise ValidationError("Nie można tworzyć rezerwacji w przeszłości.")

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(end__gt=F("start")),
                name="reservation_end_after_start",
            )
        ]
        ordering = ["start"]

    def __str__(self):
        return f"{self.room} | {self.start:%Y-%m-%d %H:%M} - {self.end:%H:%M} | {self.title}"