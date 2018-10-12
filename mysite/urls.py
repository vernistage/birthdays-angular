from django.urls import include, path
from django.contrib import admin

from rest_framework import routers

from invitations import views

router = routers.SimpleRouter()
router.register(r'events', views.EventViewSet)
router.register(r'rsvps', views.RsvpViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include(('rest_framework.urls', 'rest_framework'), namespace='rest_framework')),
    path('api/v1/invitations/', include(('invitations.urls', 'invitations'), namespace='invitations')),
    path('api/v2/', include((router.urls, 'router'), namespace='apiv2')),
]
