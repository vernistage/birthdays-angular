from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import AppUser, Event, Rsvp

class SignUpForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2', )

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['creator', 'created_at', 'last_modified']

class RsvpEditForm(ModelForm):
    class Meta:
        model = Rsvp
        fields = ['is_attending']
