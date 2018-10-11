from rest_framework import serializers

from . import models

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'birth_date',
            'first_name',
            'last_name',
            'invited_events',
        )
        model = models.AppUser

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        # extra_kwargs = {
        #     'address'
        # }
        fields = (
            'id',
            'title',
            'description',
            'address',
            'start_time',
            'creator',
            'invitees',
            'created_at',
            'last_modified'
        )
        model = models.Event

class RsvpSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'event',
            'invitee',
            'is_attending',
            'created_at',
            'last_modified'
        )
        model = models.Rsvp
