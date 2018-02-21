from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^open_link$', views.open_link, name='open _link')
url(r'^delite_link$', views.delite_link, name='delite _link')
url(r'^edit_links$', views.edit_links, name='edit_links')