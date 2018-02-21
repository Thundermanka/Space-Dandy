from django.db import models
from django.utils import timezone

class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_text = models.TextField()