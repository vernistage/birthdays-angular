from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
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

    def invite_people(self, invitee_pks):
        for k in invitees_keys:
            invitee = AppUser.objects.get(pk=k)
            Rsvp(event=self, invitee=invitee).save()

    def add_invites(self, current_rsvps, invitees_keys):
        for k in invitees_keys:
            invitee = AppUser.objects.get(pk=k)
            if not Rsvp.objects.filter(invitee=invitee).exists():
                Rsvp(event=self, invitee=invitee).save()

    def disinvite(self, current_rsvps, invitees_keys):
        for rsvp in current_rsvps:
            if rsvp.invitee.pk not in invitees_keys:
                rsvp.delete()

    def is_creator(self, user):
        return user.pk == self.creator.pk

class Rsvp(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    invitee = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    is_attending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('event', 'invitee')
