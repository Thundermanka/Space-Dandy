from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)

    def __User__(self):
        return self.user_name

    def __User__(self):
        return self.user_surname

    def __User__(self):
        return self.user_position

    def __User__(self):
        return self.user_password

    def __User__(self):
        return self.user_login

    def __User__(self):
        return self.user_mail

class UserToChat(models.Model):
    userID = models.ForeignKey('chats.Chat', related_name='users',on_delete=models.CASCADE)
    chatID = models.ForeignKey('users.User', related_name='chats',on_delete=models.CASCADE)

class UserToAnswer(models.Model):
    userID = models.ForeignKey('answers.Answer', related_name='users')
    answerID = models.ForeignKey('users.User', related_name='answers')