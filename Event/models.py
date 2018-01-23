from django.db import models
from django.utils import timezone

class Event(models.Model):
 title = models.CharField(max_length=200)
 text = models.TextField()