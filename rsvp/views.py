# rsvp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import guest
from events.models import Event
from .forms import RSVPCodeForm, RSVPForm

def home(request):
    return render(request, "rsvp/home.html")

def rsvp_home(request):
    return render(request, "rsvp/rsvp_home.html")

def rsvp_code(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        form = RSVPCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            guest = get_object_or_404(guest, event=event, code=code)
            return redirect('rsvp_guest', token=guest.code)
    else:
        form = RSVPCodeForm()

    return render(request, "rsvp/rsvp_code.html", {
        "event": event,
        "form": form
    })


def rsvp_guest(request, token):
    guest = get_object_or_404(guest, code=token)
    event = guest.event

    if request.method == "POST":
        form = RSVPForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()



            return redirect('rsvp_confirm', token=guest.code)
    else:
        form = RSVPForm(instance=guest)

    return render(request, "rsvp/rsvp.html", {
        "event": event,
        "invitation": guest,
        "form": form,
    })


def rsvp_confirm(request, token):
    invitation = get_object_or_404(guest, code=token)
    event = guest.event
    return render(request, "rsvp/rsvp_confirm.html", {
        "event": event,
        "guest": guest,
    })

def about(request):
    return render(request, "rsvp/about.html")


def contact(request):
    return render(request, "rsvp/contact.html")