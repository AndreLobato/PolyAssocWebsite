from models import UsefulLink, Event, Publication, Photo

from django.forms import ModelForm
from cmsplugin_advancednews.forms import NewsForm


class UsefulLinkForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = UsefulLink

class EventForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = Event


class PublicationForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = Publication

class PhotoForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = Photo

class CustomNewsForm(NewsForm):
    error_css_class = 'error'
    required_css_class = 'required'


