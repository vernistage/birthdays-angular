from .models import Event
from .forms import EventForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

User = get_user_model()

def welcome(request):
    return render(request, 'welcome.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login (request, user)
            return redirect('user_profile', user.pk)
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

@login_required
def user_profile(request, pk):
    return render(request, 'user_profile.html')

@login_required
def events(request):
    return True

@login_required
def event(request, pk):
    pass

@login_required
def event_new(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile', user.pk)
    else:
        form = EventForm()
    return render(request, 'event_new.html', {'form': form})

@login_required
def event_edit(request, pk):
    pass

@login_required
def event_destroy(request, pk):
    pass
