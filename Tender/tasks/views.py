from django.shortcuts import render

# Create your views here.
def view_task(request):
    return render(request, 'task/view_task.html', {})

def new_link(request):
	return render(request, 'task/new_link.html', {})

def edit_task(request):
	return render(request, 'task/edit_task.html', {})	