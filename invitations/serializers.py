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
    # rsvp_set = RsvpSerializer(many=True, read_only=True)
    # rsvp_set = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='apiv2:rsvp-detail'
    # )
    # Fastest option below just gets the integer
    rsvp_set = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    # custom serializer field
    duration = serializers.SerializerMethodField()

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
            'last_modified',
            'duration',
        )
        model = models.Event

    # custom serializer method okay for calculating on the fly (more overhead)
    def get_duration(self, obj):
        return obj.end_time - obj.start_time

    # def validate_title(self, value):
    #     if self.title.len > 3:
    #         return self.title
    #     raise serializers.ValidationError(
    #         'Title must be longer than three characters.'
    #     )
