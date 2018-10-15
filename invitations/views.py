from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models
from . import forms
from . import serializers

#API v1 views
class ListCreateEvent(generics.ListCreateAPIView):
    #Don't have to type raw JSON with generics
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Event.objects.all()
    serializer_class =serializers.EventSerializer

class ListCreateRsvp(generics.ListCreateAPIView):
    queryset = models.Rsvp.objects.all()
    serializer_class = serializers.RsvpSerializer

    def get_queryset(self):
        return self.queryset.filter(event_id=self.kwargs.get('event_pk'))

    def perform_create(self, serializer):
        event = get_object_or_404(
            models.Event, pk=self.kwargs.get('event_pk'))
        serializer.save(event=event)

class RetrieveUpdateDestroyRsvp(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Rsvp.objects.all()
    serializer_class =serializers.RsvpSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            event_id=self.kwargs.get('event_pk'),
            pk=self.kwargs.get('pk')
        )

#API V2
class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    # Only using this route to get events
    @detail_route(methods=['get'])
    def rsvps(self, request, pk=None):
        event = self.get_object()
        serializer = serializers.RsvpSerializer(event.rsvp_set.all(), many=True)
        return Response(serializer.data)


class RsvpViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = models.Rsvp.objects.all()
    serializer_class = serializers.RsvpSerializer

# TODO Rsvp Detail View
