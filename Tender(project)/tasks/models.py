from django.db import models
from django.utils import timezone

class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_text = models.TextField()
    eventID = models.ForeignKey('events.Event', related_name='tasks',on_delete=models.CASCADE)
    date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __Task__(self):
        return self.task_title

    def __Task__(self):
        return self.task_text
