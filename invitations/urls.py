from . import views
from django.conf.urls import url
from invitations.views import EventView, RsvpView

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^user/(?P<pk>\d+)/$', views.user_profile, name='user_profile'),
    url(r'^event/(?P<pk>\d+)/$', views.EventView.as_view(), name='event'),
    url(r'^event/new/$', views.EventView.as_view(), name='event_new'),
    url(r'^event/(?P<pk>\d+)/edit/$', views.EventView.as_view(), name='event_edit'),
    url(r'^event/(?P<pk>\d+)/destroy/$', views.EventView.as_view(), name='event_destroy'),
    url(r'^rsvp/(?P<pk>\d+)/edit/$', views.RsvpView.as_view(), name='rsvp_edit'),
]
