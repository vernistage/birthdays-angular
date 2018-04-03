from . import views
from django.conf.urls import url
# from invitations.views import EventView, RsvpView, WelcomeView

urlpatterns = [
    url(r'^events/(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='event'),
    url(r'^events/create/$', views.EventCreateView.as_view(), name='create_event'),
    url(r'^rsvps/edit/(?P<pk>\d+)$', views.RsvpUpdateView.as_view(), name='update_rsvp'),
]
