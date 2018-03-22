from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import AppUser, Event

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')
    birth_date = forms.DateField(required=True, help_text='Required. Input your birthday.')

    class Meta:
        model = AppUser
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2', )

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'address', 'start_time', 'end_time']
