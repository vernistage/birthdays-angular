from django import forms
from django.forms import ModelForm, DateTimeField, TextInput
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
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'name'}),
        }
        help_texts = {
            'first_name': ('Some useful help text.'),
        }

class RsvpEditForm(ModelForm):
    class Meta:
        model = Rsvp
        fields = ['is_attending']
