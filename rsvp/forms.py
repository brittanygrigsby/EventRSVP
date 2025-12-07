from django import forms
from .models import guest, MEAL_CHOICES

class RSVPCodeForm(forms.Form):
    code = forms.CharField(label="RSVP Code", max_length=20)

class RSVPForm(forms.ModelForm):
    class Meta:
        model = guest
        fields = ['attending', 'meal_choice']
