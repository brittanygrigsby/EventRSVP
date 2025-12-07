from django.db import models
from events.models import Event

MEAL_CHOICES = [
    ('steak', 'Steak'),
    ('chicken', 'Chicken'),
    ('vegetarian', 'Vegetarian'),
    ('vegan', 'Vegan'),
]

class guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='guests')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    code = models.CharField(max_length=20, unique=True)

    attending = models.BooleanField(null=True, blank=True)
    meal_choice = models.CharField(max_length=20, choices=MEAL_CHOICES, blank=True)

    def __str__(self):
        return f"{self.name} - {self.event.name}"
