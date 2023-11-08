from django.shortcuts import render

def home(request):
    return render(request, 'app1/home.html', {})

def contact(request):
    return render(request, 'app1/contact.html', {})

def projects(request):
    return render(request, 'app1/projects.html', {})

def games(request):
    return render(request, 'app1/games.html', {})

def ds(request):
    return render(request, 'app1/ds.html', {})
