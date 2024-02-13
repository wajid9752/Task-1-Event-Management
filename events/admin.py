from django.contrib import admin
from .models import Event , EventRegistration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        "organizer",
        "title",
        "description",
        "location",
        "registration_deadline",
        "event_day",
        "featured_image",
        "status"
    ]

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "event"
    ]