from models import UsefulLink, Event, Publication
from django.forms import ModelForm

class UsefulLinkForm(ModelForm):
     class Meta:    
        model = UsefulLink

class EventForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = Event
