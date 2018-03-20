from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^events/$', views.events, name='events'),
    url(r'^event/(?P<pk>\d+)/$', views.event, name='event'),
    url(r'^event/new/$', views.event_new, name='event_new'),
    url(r'^event/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^event/(?P<pk>\d+)/destroy/$', views.event_destroy, name='event_destroy'),
]
