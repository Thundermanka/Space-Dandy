from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^User/', include('users.urls')), 
    url(r'^Task/', include('tasks.urls')), 
    url(r'^Event/', include('events.urls')),
]