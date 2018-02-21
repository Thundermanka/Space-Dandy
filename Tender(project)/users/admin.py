from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.UserToChat)
admin.site.register(models.UserToAnswer)