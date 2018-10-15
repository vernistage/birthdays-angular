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

class EventSerializer(serializers.ModelSerializer):
    # rsvps = RsvpSerializer(many=True, read_only=True)
    rsvp_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='apiv2:rsvp-detail'
    )
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'address',
            'start_time',
            'end_time',
            'creator',
            'invitees',
            'rsvp_set',
            'created_at',
            'last_modified'
        )
        model = models.Event
