from django.contrib import admin
from .models import Guest

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "event", "code", "attending", "meal_choice")
    list_filter = ("event", "attending", "meal_choice")
    search_fields = ("name", "email", "code")
