from django.shortcuts import render
from django.utils import timezone
from .models import Event
# Create your views here.
def new_event(request):
	events = Event.object.order_by('event_title')
	return render(request, 'events/new_event.html', {'events': events})

def list(request):
	events = Event.object.order_by('date_start')
	return render(request, 'events/events_list.html', {'events': events})

def new_task(request):
	events = Event.object.order_by('event_title')
	return render(request, 'events/create_task.html', {'events': events})

def task_list(request):
	events = Event.object.order_by('date_end')
	return render(request, 'events/task_list.html', {'events': events})

def new_link(request):
	events = Event.object.order_by('event_title')
	return render(request, 'events/new_link.html', {'events': events})	

def edit_event(request):
	events = Event.object.order_by('event_text')
	return render(request, 'events/edit_event.html', {'events': events})