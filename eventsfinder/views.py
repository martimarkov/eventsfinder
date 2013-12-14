from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template.context import RequestContext

def home(request):
    return render(request, 'home.html')

def add_event(request):
    return render(request, 'add_event.html')

def find_events(request):
    return render(request, 'find_events.html')

def manage_events(request):
    return render(request, 'manage_events.html')




def signup(request):

    form = request.POST.get("form", "")

    if request.method =='POST':
        form = UserCreationForm(request.POST)

    if form:
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password1'])
            login(request, user)
            return redirect('home') # Redirect after POST
    else:
        form = UserCreationForm() # An unbound form

    return render_to_response('signup.html', { 'form': form, }, context_instance=RequestContext(request))
