from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def add_event(request):
    return render(request, 'add_event.html')