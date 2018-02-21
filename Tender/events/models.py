from django.db import models
from django.utils import timezone

class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_text = models.TextField()
    date_start = models.DateTimeField(
        default=timezone.now)
    date_end = models.DateTimeField(
        default=timezone.now)