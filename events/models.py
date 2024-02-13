from django.db import models
from accounts.models import BaseClass,CustomUser



class Event(BaseClass):
    
    EVENT_STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]
    organizer   = models.ForeignKey(CustomUser , on_delete = models.CASCADE , related_name="myEvents")
    title       = models.CharField(max_length=255)
    description =  models.TextField()
    location    = models.CharField(max_length=100)

    registration_deadline = models.DateField()
    event_day             = models.DateField()
    featured_image        = models.ImageField(upload_to='event_images/')
    status                = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES, default='upcoming')
    
    def __str__(self):
        return self.title

class EventRegistration(BaseClass):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , related_name="registerdEvents")
    event = models.ForeignKey(Event, on_delete=models.CASCADE , related_name="eventParticipants")

    def __str__(self):
        return self.user.username +" registerd for "+ self.event.title
