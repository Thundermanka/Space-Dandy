from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login$', views.login, name='login'),
	url(r'^list$', views.list, name='list'),
	url(r'^logout$', views.logout, name='logout'),
]