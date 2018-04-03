from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^events/(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='event'),
    url(r'^events/create/$', views.EventCreateView.as_view(), name='create_event'),
    url(r'^events/edit/(?P<pk>\d+)/$', views.EventUpdateView.as_view(), name='update_event'),
    url(r'^events/destroy/(?P<pk>\d+)/$', views.EventDeleteView.as_view(), name='destroy_event'),
    url(r'^rsvps/edit/(?P<pk>\d+)$', views.RsvpUpdateView.as_view(), name='update_rsvp'),
]
