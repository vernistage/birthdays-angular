from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Event
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

AppUser = get_user_model()

def welcome(request):
    return render(request, 'welcome.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            AppUser = authenticate(username=username, password=raw_password)
            login (request, AppUser)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

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
