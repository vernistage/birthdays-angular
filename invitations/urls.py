from . import views
from django.urls import include, path

urlpatterns = [
    path('events/$', views.ListCreateEvent.as_view(), name='event_list'),
    path('events/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyCourse.as_view(),
        name='event_detail'),
    path('events/(?P<event_pk>\d+)/rsvps/$',
        views.ListCreateRsvp.as_view(),
        name='rsvp_list'),
    path('events/(?P<event_pk>\d+)/rsvps/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyRsvp.as_view(),
        name='rsvp_detail')
]
