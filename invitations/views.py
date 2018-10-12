from django.shortcuts import get_object_or_404

from rest_framework import generics

from . import models
from . import forms
from . import serializers

# User = get_user_model()
#
# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login (request, user)
#             return redirect('user_profile', user.pk)
#         else:
#             return render(request, 'invitations/register.html', {'form': form})
#
#     else:
#         form = SignUpForm()
#         return render(request, 'invitations/register.html', {'form': form})

#API views
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

#Django views
# class AppUserDetailView(DetailView):
#     model = AppUser
#
# class WelcomeView(TemplateView):
#     template_name = 'welcome.html'
#
#     def get_context_data(self, **kwargs):
#         user = self.request.user
#         context = super().get_context_data(**kwargs)
#         context["authenticated"] = user.is_authenticated
#         context["username"] = user.username
#         return context
#
# class EventListView(ListView):
#     model = Event
#
#     def get_context_data(self, **kwargs):
#         user = self.request.user
#         context = super().get_context_data(**kwargs)
#         context["event_list"] = Event.objects.filter(creator=user)
#         return context
#
# class EventDetailView(DetailView):
#     model = Event
#
#     def get_context_data(self, **kwargs):
#         event = self.get_object()
#         user = self.request.user
#         context = super().get_context_data(**kwargs)
#         context["is_creator"] = (event.creator == user)
#         context["is_invited"] = (user in event.invitees.all())
#         try:
#             context["rsvp"] = Rsvp.objects.get(event=event, invitee=user)
#             context["attendance"] = context["rsvp"].is_attending
#         except:
#             context["attendance"] = "Error"
#         return context
#
# class EventCreateView(CreateView):
#     model = Event
#     fields = ("title", "description", "address", "start_time", "end_time", "invitees")
#
#     # Exclude creator from invitees
#     def get_form(self, form_class=None):
#         form = super(EventCreateView, self).get_form(form_class)
#         form.fields["invitees"].queryset = AppUser.objects.all().exclude(pk=self.request.user.pk)
#         return form
#
#     def form_valid(self, form):
#         new_event = form.save(commit=False)
#         new_event.creator = self.request.user
#         new_event.save()
#         for person in form.cleaned_data['invitees']:
#             Rsvp.objects.get_or_create(invitee=person, event=new_event)
#         self.object = new_event
#         return HttpResponseRedirect(self.get_success_url())
#
# class EventUpdateView(UpdateView):
#     model = Event
#     fields = ("title", "description", "address", "start_time", "end_time", "invitees")
#
#     # Exclude creator from invitees
#     def get_form(self, form_class=None):
#         form = super(EventUpdateView, self).get_form(form_class)
#         form.fields["invitees"].queryset = AppUser.objects.all().exclude(pk=self.request.user.pk)
#         return form
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         for person in form.cleaned_data['invitees']:
#             Rsvp.objects.get_or_create(invitee=person, event=self.object)
#         self.object.save()
#         return super(ModelFormMixin, self).form_valid(form)
#
# class EventDeleteView(DeleteView):
#     model = Event
#     success_url = reverse_lazy("invitations:events")
#
# class RsvpListView(ListView):
#     model = Rsvp
#
#     def get_context_data(self, **kwargs):
#         user = self.request.user
#         context = super().get_context_data(**kwargs)
#         context["event_list"] = user.invited_events.all()
#         return context
#
# class RsvpUpdateView(UpdateView):
#     model = Rsvp
#     fields = ("is_attending",)
#
#     def form_valid(self, form):
#         rsvp = form.save()
#         return HttpResponseRedirect(self.get_success_url())
