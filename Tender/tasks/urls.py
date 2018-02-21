from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^(?P<task_id>\\d+)/$', views.view_task, name='view_task'),
url(r'^add_link$', views.new_link, name='new_link'),
url(r'^edit_task$', views.edit_task, name='edit_task')
]