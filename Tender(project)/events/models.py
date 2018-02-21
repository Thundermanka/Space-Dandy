from django.db import models
from django.utils import timezone

class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_text = models.TextField()

    def __Event__(self):
        return self.event_title

    def __Event__(self):
        return self.text