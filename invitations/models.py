from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    birth_date = models.DateField()
    invited_events = models.ManyToManyField(
        'Event',
        through='Rsvp',
        through_fields=('invitee', 'event'),
    )

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creator = models.ForeignKey(
        'AppUser',
        on_delete=models.CASCADE,
        related_name="event_rsvps")
    invitees = models.ManyToManyField(
        'AppUser',
        through='Rsvp',
        through_fields=('event', 'invitee'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Rsvp(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    invitee = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    is_attending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
