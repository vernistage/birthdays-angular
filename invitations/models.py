from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse

class AppUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    invited_events = models.ManyToManyField(
        'Event',
        through='Rsvp',
        through_fields=('invitee', 'event'),
    )

    def __str__(self):
        return self.first_name

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

    def clean_invitees(self):
        data = self.cleaned_data['invitees']
        invitees.exclude(self.creator)
        return data

    def __str__(self):
        return self.title

    def is_creator(self, user):
        user.pk == self.creator.pk

    def get_absolute_url(self):
        return reverse("invitations:event", kwargs={"pk": self.pk})

    def get_invitees(self):
        return self.invitees.all()

    def confirmed_yes(self):
        rsvpd_yes = []
        for rsvp in self.rsvp_set.all():
            if rsvp.is_attending:
                rsvpd_yes.append(rsvp)
        return rsvpd_yes



class Rsvp(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    invitee = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    is_attending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('event', 'invitee')

    def get_absolute_url(self):
        return reverse("invitations:event", kwargs={"pk": self.event.pk})
