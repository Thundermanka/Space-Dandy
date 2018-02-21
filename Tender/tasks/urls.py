from django.conf.urls import url
from . import views

urlpatterns = [
url (r'^list_task$', views.list_tasks, name='list_tasks'),
url (r'^(?P<event_id>\\d+)/$', views.Event, name='Событие'),
url (r'^add_link$', views.new_link, name='new_link'),
]