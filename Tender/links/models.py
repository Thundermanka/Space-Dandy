from django.db import models
from django.utils import timezone

class Link(models.Model):
    link_title = models.CharField(max_length=200)
    link_adress = models.TextField()
    eventID = models.ForeignKey('events.Event', related_name='links',on_delete=models.CASCADE)
    taskID = models.ForeignKey('tasks.Task', related_name='links',on_delete=models.CASCADE)

    def __Link__(self):
        return self.link_title

    def __Link__(self):
        return self.link_adress