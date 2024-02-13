from django import forms
from .models import Event

class CreateEventForm(forms.ModelForm):
    class Meta:
        model   = Event
        fields  = [
            "title",
            "description",
            "location",
            "registration_deadline",
            "event_day",
            "featured_image",
            "status"
        ]
        
        widgets = {
            "title":  forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 5}),
            "location":  forms.TextInput(attrs={'class': 'form-control'}),
            "registration_deadline": forms.widgets.DateInput(attrs={'class': 'form-control' , 'type': 'date'}),
            "event_day": forms.widgets.DateInput(attrs={'class': 'form-control' , 'type': 'date'}),
            "featured_image": forms.widgets.FileInput(attrs={'accept': 'image/*' , 'class': 'form-control' }) ,
            "status": forms.Select(attrs={'class': 'form-control product_id'}),
        }

