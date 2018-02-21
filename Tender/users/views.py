from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'users/users_list.html', {})

def logout(request):
    return render(request, 'users/start_page.html', {})

def login(request):
    return render(request, 'users/login_page.html', {})