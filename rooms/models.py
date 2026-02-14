from django.db import models
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
