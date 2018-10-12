from . import views
from django.conf.urls import url
# from django.contrib.auth.decorators import login_required

app_name = "invitations"

urlpatterns = [
    url(r'^events/$', views.ListCreateEvent.as_view(), name='event_list'),
    url(r'^events/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyCourse.as_view(),
        name='event_detail'),
    url(r'^events/(?P<event_pk>\d+)/rsvps/$',
        views.ListCreateRsvp.as_view(),
        name='rsvp_list'),
    url(r'^events/(?P<event_pk>\d+)/rsvps/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyRsvp.as_view(),
        name='rsvp_detail'),
    # url(r'^events/$', login_required(views.EventListView.as_view()), name='events'),
    # url(r'^events/(?P<pk>\d+)/$', login_required(views.EventDetailView.as_view()), name='event'),
    # url(r'^events/create/$', login_required(views.EventCreateView.as_view()), name='create_event'),
    # url(r'^events/edit/(?P<pk>\d+)/$', login_required(views.EventUpdateView.as_view()), name='update_event'),
    # url(r'^events/destroy/(?P<pk>\d+)/$', login_required(views.EventDeleteView.as_view()), name='destroy_event'),
    # url(r'^rsvps/$', login_required(views.RsvpListView.as_view()), name='rsvps'),
    # url(r'^rsvps/edit/(?P<pk>\d+)$', login_required(views.RsvpUpdateView.as_view()), name='update_rsvp'),
]
