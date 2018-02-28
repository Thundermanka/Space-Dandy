from django.shortcuts import render
from django.utils import timezone
from .models import Link
# Create your views here.
def open_link(request):
    links = Link.object.order_by('link_title')
    return redirect("https://yandex.ru/")

def delite_link(request):
    links = Link.object.order_by('link_title')
    return redirect('/')

def edit_links(request):
	links = Link.object.order_by('link_adress')
	return render(request, 'links/edit_links.html', {'links': links})