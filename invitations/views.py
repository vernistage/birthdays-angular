from .models import (
    Event, AppUser,
    Rsvp
)
from .forms import (
    EventForm, EventForm,
    RsvpEditForm
)
from django.shortcuts import (
    render, get_object_or_404,
    redirect
)
from django.contrib.auth import (
    login, authenticate,
    get_user_model
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    View, TemplateView,
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)
from .forms import SignUpForm

User = get_user_model()

class WelcomeView(TemplateView):
    template_name = 'welcome.html'
    # https://teamtreehouse.com/library/templateview
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["authenticated"] = user.is_authenticated
        context["username"] = user.username
        return context

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login (request, user)
            return redirect('user_profile', user.pk)
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def user_profile(request, pk):
    events = Event.objects.filter(creator=request.user)
    invitations = request.user.invited_events.all()
    invitation_count = request.user.invited_events.all().count()
    event_count = events.count()
    to_rsvps = None
    if Rsvp.objects.filter(invitee=request.user).exists():
        to_rsvps = Rsvp.objects.filter(invitee=request.user)
    return render(request, 'user_profile.html', {'events': events, 'event_count': event_count, 'invitations': invitations, 'invitation_count': invitation_count, 'to_rsvps': to_rsvps})

class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        rsvp = Rsvp.objects.get(event=self.get_object(), invitee=self.request.user)
        context = super().get_context_data(**kwargs)
        context["attendance"] = rsvp.is_attending
        return context

class EventCreateView(CreateView):
    model = Event
    fields = ("title", "description", "address", "start_time", "end_time", "invitees")

    def form_valid(self, form):
        new_event = form.save(commit=False)
        new_event.creator = self.request.user
        new_event.save()
        print(new_event.invitees)
        return HttpResponseRedirect(self.get_success_url())

class RsvpUpdateView(UpdateView):
    model = Rsvp
    fields = ("is_attending",)

    def form_valid(self, form):
        rsvp = form.save()
        return HttpResponseRedirect(self.get_success_url())
