from django.shortcuts import render

def homeRequest(request):
    return render(request, 'home.html')