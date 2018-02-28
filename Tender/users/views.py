from django.shortcuts import render
from django.utils import timezone
from .models import User
# Create your views here.
def list(request):
    users = User.object.order_by('surname')
    return render(request, 'users/users_list.html', {'users': users})

def logout(request):
    users = User.object.order_by('password')
    return render(request, 'users/start_page.html', {'users': users})

def login(request):
    users = User.object.order_by('login')
    return render(request, 'users/login_page.html', {'users': users})