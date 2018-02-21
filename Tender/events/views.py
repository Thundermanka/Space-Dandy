from django.shortcuts import render

# Create your views here.
def new_event(request):
    return render(request, 'events/new_event.html', {})

def list(request):
    return render(request, 'events/events_list.html', {})

def new_task(request):
	return render(request, 'events/create_task.html', {})

def task_list(request):
	return render(request, 'events/task_list.html', {})	

def new_link(request):
	return render(request, 'events/new_link.html', {})	

def edit_event(request):
	return render(request, 'events/edit_event.html', {})