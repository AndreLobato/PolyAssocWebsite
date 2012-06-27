from haystack.indexes import *
from haystack import site
from cms.models import Page, Title
from poly_assoc_website.models import MemberProfile, Publication, Event, UsefulLink, Photo

class PageIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    created_by = CharField(model_attr='user')
    publication_date = DateTimeField(model_attr='publication_date')
   

class PublicationIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    author = CharField(model_attr='author')
    others_authors = CharField(model_attr='others_authors')
    publisher = CharField(model_attr='publisher')
    url = CharField(model_attr='url')
    publication_date = DateTimeField(model_attr='publish_date')

class MemberIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    about_me = CharField(model_attr='about_me')
    institution = CharField(model_attr='institution')
    work_location = CharField(model_attr='work_location')
    research_area = CharField(model_attr='research_area')
    homepage_url = CharField(model_attr='homepage_url')


class UsefulLinkIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    url = CharField(model_attr='url')
    description = CharField(model_attr='description')

    
class EventIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    location = CharField(model_attr='location')
    url = CharField(model_attr='url')
    details = CharField(model_attr='details')

class PhotoIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    name = CharField(model_attr='name')
    description = CharField(model_attr='description')

site.register(Page, PageIndex)
site.register(Publication, PublicationIndex)
site.register(MemberProfile, MemberIndex)
site.register(UsefulLink, UsefulLinkIndex)
site.register(Event, EventIndex)
site.register(Photo, PhotoIndex)