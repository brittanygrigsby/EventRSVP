from django.contrib import admin
from .models import guest

@admin.register(guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "event", "code", "attending", "meal_choice")
    list_filter = ("event", "attending", "meal_choice")
    search_fields = ("name", "email", "code")
