from django.db import models
from django.utils import timezone

class Chat(models.Model):
    title = models.CharField(max_length=200)
