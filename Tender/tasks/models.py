from django.db import models
from django.utils import timezone

class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_text = models.TextField()
    eventID = models.ForeignKey('events.Event', related_name='tasks',on_delete=models.CASCADE)
    date = models.DateTimeField(
        default=timezone.now)