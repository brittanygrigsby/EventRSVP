# events/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event


def event_list(request):
    events = Event.objects.all().order_by("date")
    return render(request, "events/events.html", {"events": events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "events/event_detail.html", {"event": event})


@login_required
def host_dashboard(request):
    events = Event.objects.all().order_by("date")
    context = {"events": events}
    return render(request, "events/host_dashboard.html", context)


@login_required
def event_create(request):
    # create form for host to create events 
    return render(request, "events/event_create.html")


@login_required
def event_edit(request, event_id):

    # create form to edit events only avail for host
    return render(request, "events/event_edit.html")


@login_required
def event_guests(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    guests = event.guests.all() if hasattr(event, "guests") else []
    context = {"event": event, "guests": guests}
    return render(request, "events/event_guests.html", context)
