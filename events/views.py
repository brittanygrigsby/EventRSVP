from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from .models import Event
from .forms import EventForm
from django.conf import settings
from rsvp.models import Guest
from .forms import GuestInviteForm
from rsvp.forms import RSVPForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def event_list(request):
    events = Event.objects.all().order_by("date")
    return render(request, "events/event_list.html", {"events": events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    guest = None
    rsvp_form = None
    error = None

    if request.method == "POST" and request.POST.get("guest_code_submit") == "1":
        code = request.POST.get("code", "").strip().upper()

        try:
            guest = Guest.objects.get(event=event, code=code)
            rsvp_form = RSVPForm(instance=guest)
        except Guest.DoesNotExist:
            error = "Sorry, that guest code does not match our records."
            messages.error(request, error) 


    elif request.method == "POST" and request.POST.get("rsvp_submit") == "1":
        guest_id = request.POST.get("guest_id")
        guest = get_object_or_404(Guest, id=guest_id, event=event)

        rsvp_form = RSVPForm(request.POST, instance=guest)
        if rsvp_form.is_valid():
            rsvp_form.save()
        messages.success(request, "RSVP saved! Thank you.")
        return redirect("rsvp:rsvp_confirm", event_id=event.id)


    return render(request, "events/event_detail.html", {
        "event": event,
        "guest": guest,
        "rsvp_form": rsvp_form,
        "error": error,
    })

#HOST ACCOUNT SIGN UP
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("events:host_dashboard")
    else:
        form = UserCreationForm()

    return render(request, "events/signup.html", {"form": form})



@login_required
def host_dashboard(request):
    events = Event.objects.all().order_by("date")
    context = {"events": events}
    return render(request, "events/host_dashboard.html", {"events": events})


@login_required
def event_edit(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect("events:event_detail", event_id=event.id)
    else:
        form = EventForm(instance=event)

    return render(request, "events/event_edit.html", {"form": form, "event": event})


@login_required
def event_guests(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        form = GuestInviteForm(request.POST)

        if form.is_valid():
            first = form.cleaned_data.get("first_name", "").strip()
            last = form.cleaned_data.get("last_name", "").strip()
            email = form.cleaned_data.get("email", "").strip()

            # duplicate check
            if Guest.objects.filter(event=event, email__iexact=email).exists():
                form.add_error("email", "Guest already exists for this event.")
            else:
                full_name = f"{first} {last}"

                guest = Guest(event=event, name=full_name, email=email)
                guest.save()


                subject = f"You're invited to {event.name}!"
                message = (
                    f"Hi {guest.name},\n\n"
                    f"You've been invited to {event.name} on {event.date}.\n\n"
                    f"Your guest code is: {guest.code}\n\n"
                    f"Use this code on the event page to RSVP.\n\n"
                    f"Thanks!"
                )

                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [guest.email],
                    fail_silently=False,
                )


                messages.success(request, f"Invite sent to {guest.email}.")
                return redirect("events:event_guests", event_id=event.id)

  
    else:
        form = GuestInviteForm()

    guests = Guest.objects.filter(event=event).order_by("-id")
    return render(request, "events/event_guests.html", {"event": event, "guests": guests, "form": form})




@login_required
@require_POST
def guest_delete(request, event_id, guest_id):
    event = get_object_or_404(Event, id=event_id)
    guest = get_object_or_404(Guest, id=guest_id, event=event)

    guest_email = guest.email
    guest.delete()

    messages.success(request, f"Guest removed: {guest_email}. You can re-add and resend anytime.")
    return redirect("events:event_guests", event_id=event.id)


@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.host = request.user
            event.save()
            messages.success(request, "Your event was created successfully! 🎉")
            return redirect("events:event_list") 
    else:
        form = EventForm()

    return render(request, "events/event_create.html", {"form": form})

@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        event.delete()
        messages.success(request, "Your event was deleted.")
        return redirect("events:event_list")

    return redirect("events:event_detail", event_id=event_id)