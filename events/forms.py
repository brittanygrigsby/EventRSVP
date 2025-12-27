from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={"type": "time"})
    )

    class Meta:
        model = Event
        fields = ["name", "date", "description", "image", "time", "registry_url"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Event Name Here"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Add special notes for your guests..."}),
        }



class GuestInviteForm(forms.Form):
    first_name = forms.CharField(
        max_length=60,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "First name"})
    )
    last_name = forms.CharField(
        max_length=60,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Last name"})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email address"})
    )
    
