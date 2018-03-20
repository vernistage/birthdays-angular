from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Event
# from .forms import EventForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request, 'welcome.html')

def register(request):
    pass

@login_required
def events(request):
    return True

@login_required
def event(request, pk):
    pass

@login_required
def event_new(request):
    pass

@login_required
def event_edit(request, pk):
    pass

@login_required
def event_destroy(request, pk):
    pass
