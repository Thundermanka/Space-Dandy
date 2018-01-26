from django.db import models
from django.utils import timezone

class Answer(models.Model):
text = models.TextField()
messageTemplate = models.ForeignKey('MessageTemplate.MessageTemplate', related_name='answers')

class Chat(models.Model):
title = models.CharField(max_length=200)
event = models.ForeignKey('Event.Event', related_name='chats')
task = models.ForeignKey('Task.Task', related_name='chats')

class Event(models.Model):
title = models.CharField(max_length=200)
text = models.TextField()

from mysite.settings import MEDIA_ROOT

class File(models.Model):
file = models.FileField(upload_to=MEDIA_ROOT, max_length=100)
task = models.ForeignKey('Task.Task', related_name='files')
message = models.ForeignKey('Message.Message', related_name='files')
event = models.ForeignKey('Event.Event', related_name='files')
type = models.TextField()

class Link(models.Model):
title = models.CharField(max_length=200)
adress = models.TextField()
event = models.ForeignKey('Event.Event', related_name='links')
task = models.ForeignKey('Task.Task', related_name='links')

class Message(models.Model):
text = models.TextField()
chat = models.ForeignKey('Chat.Chat', related_name='messages')
user = models.ForeignKey('User.User', related_name='messages')
date = models.DateTimeField(
default=timezone.now)

class Task(models.Model):
title = models.CharField(max_length=200)
text = models.TextField()
event = models.ForeignKey('Event.Event', related_name='tasks')
date = models.DateTimeField(
default=timezone.now)

class User(models.Model):
name = models.CharField(max_length=200)
surname = models.CharField(max_length=200)
position = models.CharField(max_length=200)
password = models.CharField(max_length=200)
login = models.CharField(max_length=200)
mail = models.CharField(max_length=200)

class UserToChat(models.Model):
userID = models.ForeignKey('Chat.Chat', related_name='users')
chatID = models.ForeignKey('User.User', related_name='chats')

class UserToAnswer(models.Model):
userID = models.ForeignKey('Answer.Answer', related_name='users')
answerID = models.ForeignKey('User.User', related_name='answers')