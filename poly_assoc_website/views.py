# Create your views here.

import datetime

from django.contrib.auth import logout
from django.core.context_processors import csrf
from django.views.generic.simple import direct_to_template
from django.views.generic.date_based import archive_index
from django.views.generic import list_detail
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.views.defaults import RequestContext
from django.http import Http404, HttpResponse
from userena.decorators import secure_required
from guardian.decorators import permission_required_or_403
import datetime as dt


from django.template import TemplateDoesNotExist
from poly_assoc_website.forms import UsefulLinkForm, EventForm, PublicationForm
from poly_assoc_website.models import MemberProfile, Event, Publication, UsefulLink, Photo
from poly_assoc_website.views import *


def signout(request):
    logout(request)
    return direct_to_template(request, "logout_complete.html")


def useful_links(request):
    return list_detail.object_list(request, UsefulLink.objects.all())

def add_note(request):
    request.POST
    


def new_useful_link(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = UsefulLinkForm(request.POST)
        if form.is_valid:
            form.save()
        else:
            form = UsefulLinkForm(request.POST)
    else:
        form = UsefulLinkForm()
    try:
        return render_to_response('poly_assoc_website/new_useful_link.html', {'form' : form }, RequestContext(request))
    except TemplateDoesNotExist:
        raise Http404()


def load_base_page(request):  
    return direct_to_template(request,'base.html')

def latest_links(request):
    all_links = UsefulLink.objects.all()
    return archive_index(request, all_links, 'datetime', 7, extra_context={'total_links' : all_links.count() } )

@secure_required
@permission_required_or_403('event_add')
def add_event(request):
    c = {}
    c.update(csrf(request))
	
    if request.method == 'POST':
        event_data = {'event_type' : request.POST['event_type'],
                      'title' : request.POST['title'],
                      'event_datetime' : request.POST['event_datetime'],
                      'location' :  request.POST['location'],
                      'url' : request.POST['url'],
                      'details' : request.POST['details'],
                      'posted_by' : request.POST['posted_by'],}    
        event = EventForm(event_data,auto_id=True)
        if event.is_valid():          
            event.save()
            return redirect('/event/add/complete/')         
        else:           
            event.error = "Event did not validate."       
            return render_to_response('poly_assoc_website/event_add.html', {'form' : event }, RequestContext(request))
         
 
    if request.method == 'GET':
        event = EventForm(auto_id=True)       
        try:
            return render_to_response('poly_assoc_website/event_add.html', {'form' : event }, RequestContext(request))
        except TemplateDoesNotExist:
            raise Http404() 
        
def event_detail(request):  
    events = Event.objects.all()
    return list_detail.object_detail(request,queryset=events, object_id=request.GET['event_id'],
                                    template_object_name='event')
    

def show_all_events(request):
    return list_detail.object_list(request, Event.objects.all())
    

def publications(request):
    publications = Publication.objects.all()
    return list_detail.object_list(request,queryset=publications)

def my_publications(request, user):       
        my_publications = Publication.objects.filter(author=user)
        return direct_to_template(request, "poly_assoc_website/my_publication_list.html",
                                  {'object_list' : my_publications } )


@secure_required
@permission_required_or_403('publication_add')
def publication_add(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        publication = PublicationForm(request.method['POST'], auto_id=True)
        if publication.is_valid():
            publication.save()
        else:
            publication.error = "Publication did not validate."
            return render_to_response('poly_assoc_website/publication_add.html', {'form' : publication }, RequestContext(request))
    if request.method == 'GET':
        publication = PublicationForm(auto_id=True)
        try:
            return render_to_response('poly_assoc_website/publication_add.html', {'form' : publication }, RequestContext(request))
        except TemplateDoesNotExist:
            raise Http404() 
    



def publications_detail(request):   
    object_id = request.user.id
    return list_detail.object_detail(request,queryset=events, 
                    object_id=object_id)

def photo_gallery(request):
    photos = Photo.objects.all()
    return list_detail.object_list(request, queryset=photos,
                  template_name="poly_assoc_website/photo_gallery.html",)

def photo_detail(request, name_photo):
    photo = Photo.objects.get(name=name_photo)
    return list_detail.object_detail(request, queryset=Photo.objects.all(), object_id=photo.id ,template_object_name='photo')

def members_list(request):
    return list_detail.object_list(request, queryset=MemberProfile.objects.all())

def member_profile(request, username):
    user = User.objects.get(username=username)
    member = MemberProfile.objects.get(user=user.id)
    return direct_to_template(request, template="poly_assoc_website/memberprofile_detail.html", extra_context={'object' : member})























