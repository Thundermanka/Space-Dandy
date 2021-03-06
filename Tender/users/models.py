from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)

class UserToTask(models.Model):
 	userID = models.ForeignKey('users.User', related_name='tasks',on_delete=models.CASCADE)
 	taskID = models.ForeignKey('tasks.Task', related_name='users',on_delete=models.CASCADE)