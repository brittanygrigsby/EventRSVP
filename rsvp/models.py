from django.db import models
from django.utils.crypto import get_random_string

class Guest(models.Model):
    event = models.ForeignKey("events.Event", on_delete=models.CASCADE, related_name="guests")

    name = models.CharField(max_length=120)
    email = models.EmailField()

    code = models.CharField(max_length=12, unique=True, editable=False)

    attending = models.BooleanField(null=True, blank=True)

    MEAL_CHOICES = [
        ("chicken", "Chicken"),
        ("beef", "Beef"),
        ("fish", "Fish"),
        ("veg", "Vegetarian"),
    ]
    
    meal_choice = models.CharField(max_length=20, choices=MEAL_CHOICES, blank=True)

    plus_one = models.BooleanField(default=False)
    
    plus_one_meal_choice = models.CharField(max_length=20, choices=MEAL_CHOICES, blank=True)
    plus_one_meal_choice = models.CharField(
        max_length=20,
        choices=MEAL_CHOICES,
        blank=True
    )
    
    def save(self, *args, **kwargs):
        if not self.code:
            while True:
                candidate = get_random_string(10).upper()
                if not Guest.objects.filter(code=candidate).exists():
                    self.code = candidate
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.email}"
