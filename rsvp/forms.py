from django import forms
from .models import Guest

class RSVPCodeForm(forms.Form):
    code = forms.CharField(label="RSVP Code", max_length=20)

class RSVPForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ["attending", "meal_choice", "plus_one", "plus_one_meal_choice"]
        labels = {
            "attending": "Will you be attending?",
            "meal_choice": "Meal preference",
            "plus_one": "Bringing a plus one?",
            "plus_one_meal_choice": "Plus-one meal preference",
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")
