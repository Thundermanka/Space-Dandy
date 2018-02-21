from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^new_event$', views.new_event, name='new_event'),
url(r'^list$', views.list, name='list'),
url(r' ^add_task$', views.new_task, name='new_task'),
url(r'^add_link$', views.new_link, name='new_link'),
url(r'^edit_event$', views.edit_event, name='edit_event'), 
url(r'^(?P<event_id>\\d+)/task_list/$', views.task_list, name='task_list'),
]
