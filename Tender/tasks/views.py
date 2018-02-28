from django.shortcuts import render
from django.utils import timezone
from .models import Task
# Create your views here.
def view_task(request):
    tasks = Task.object.order_by('task_title')
    return render(request, 'task/view_task.html', {'tasks': tasks})

def new_link(request):
	tasks = Task.object.order_by('task_text')
	return render(request, 'task/new_link.html', {'tasks': tasks})

def edit_task(request):
	tasks = Task.object.order_by('date')
	return render(request, 'task/edit_task.html', {'tasks': tasks})	