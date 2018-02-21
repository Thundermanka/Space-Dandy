from django.shortcuts import render

# Create your views here.
def open_link(request):
    return redirect("https://yandex.ru/")

def delite_link(request):
    return redirect('/')

def edit_links(request):
	return render(request, 'links/edit_links.html', {})