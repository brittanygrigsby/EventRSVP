from django import forms
from .models import guest, MEAL_CHOICES

class RSVPCodeForm(forms.Form):
    code = forms.CharField(label="RSVP Code", max_length=20)

class RSVPForm(forms.ModelForm):
    class Meta:
        model = guest
        fields = ['attending', 'meal_choice']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")
