from . import views
from django.conf.urls import url
from invitations.views import EventView, RsvpView, WelcomeView

urlpatterns = [
    url(r'^$', views.WelcomeView.as_view(), name='welcome'),
    url(r'^user/(?P<pk>\d+)/$', views.user_profile, name='user_profile'),
    url(r'^events/create/$', views.EventCreateView.as_view(), name='create_event'),
    url(r'^events/(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='event'),
]
