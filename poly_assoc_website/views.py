# Create your views here.

import datetime

from django.contrib.auth import logout
from django.core.context_processors import csrf
from django.views.generic.simple import direct_to_template
from django.views.generic.date_based import archive_index
from django.views.generic import list_detail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render_to_response, redirect
from django.views.defaults import RequestContext
from django.http import Http404, HttpResponse
import datetime as dt


from django.template import TemplateDoesNotExist
from django.core.exceptions import ObjectDoesNotExist
from poly_assoc_website.forms import UsefulLinkForm, EventForm, PublicationForm, PhotoForm
from poly_assoc_website.models import MemberProfile, Event, Publication,UsefulLink, Photo
from poly_assoc_website.views import *
from cmsplugin_advancednews.forms import NewsForm

def signout(request):
    logout(request)
    return direct_to_template(request, "logout_complete.html")


def useful_links(request):
    return list_detail.object_list(request, UsefulLink.objects.all())

def add_note(request):
    request.POST

@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.add_usefullink'))
def new_useful_link(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        link = UsefulLinkForm(request.POST)
        if link.is_valid:
            link.save()
        else:
            link = UsefulLinkForm(request.POST)
            link.error = 'Data format did not validate.'
            return render_to_response('poly_assoc_website/userfullink_add.html', {'form' : link }, RequestContext(request))
    else:
        link = UsefulLinkForm()
    try:
        return render_to_response('poly_assoc_website/usefullink_add.html', {'form' : link }, RequestContext(request))
    except TemplateDoesNotExist:
        raise Http404()


def load_base_page(request):  
    return direct_to_template(request,'base.html')

def latest_links(request):
    all_links = UsefulLink.objects.all()
    return archive_index(request, all_links, 'datetime', 4, extra_context={'total_links' : all_links.count() } )

@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.add_event'))
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
    



def publication_detail(request,pub_id):  
    publications = Publication.objects.all()
    return list_detail.object_detail(request,queryset=publications, object_id=pub_id,
                                    template_object_name='pub')

def publications(request):
    publications = Publication.objects.all()
    return list_detail.object_list(request,queryset=publications)

def my_publications(request, user):       
        my_publications = Publication.objects.filter(author=user)
        return direct_to_template(request, "poly_assoc_website/my_publication_list.html",
                                  {'object_list' : my_publications } )


@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.add_publication'))
def add_publication(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        publication_dict = {            'title' : request.POST['title'], 
                                        'abstract' : request.POST['abstract'],
                                        'publisher' : request.POST['publisher'],
                                        'publish_date' : request.POST['publish_date'],
                                        'url' : request.POST['url'],
                                        'author' :  request.POST['author'],
                                        'others_authors' : request.POST['others_authors'],
                                        'pub_datetime': dt.datetime.now(),
                                        'posted_by': request.POST['posted_by']}
        publication = PublicationForm(publication_dict,auto_id=True)
        if publication.is_valid():
            publication.save()
            return redirect('/publication/add/complete/')
        else:
            publication.error = "Publication did not validate."
            return render_to_response('poly_assoc_website/publication_add.html', {'form' : publication }, RequestContext(request))
    if request.method == 'GET':
        publication = PublicationForm(auto_id=True)
        try:
            return render_to_response('poly_assoc_website/publication_add.html', {'form' : publication }, RequestContext(request))
        except TemplateDoesNotExist:
            raise Http404() 
    


def photo_gallery(request, photo_slug='#1'):   
    photos = Photo.objects.all()
    return list_detail.object_list(request, queryset=photos,
                  template_name = "poly_assoc_website/photo_gallery.html",
                  extra_context = {'photo_slug' : photo_slug}
                  )

def photo_detail(request, name_photo):
    try:
        photo = Photo.objects.get(slug_title=name_photo)
        return list_detail.object_detail(request, queryset=Photo.objects.all(), object_id=photo.id ,template_object_name='photo')
    except DoesNotExist:
        obj_request = name_photo 
        return direct_to_template(template='poly_assoc_website/does_not_exist.html', extra_context={'object': obj_request})
    


@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.add_photo'))
def add_photo(request): 
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        from django.template.defaultfilters import slugify
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/photos/add/complete/')
        else:
            form.error = "Photo did not validate. Maybe some fields are missing"
            return render_to_response('poly_assoc_website/photo_add.html', {'form' : form }, RequestContext(request))
    if request.method == 'GET':                         
        form = PhotoForm(auto_id=True)
        try:
            return render_to_response('poly_assoc_website/photo_add.html', {'form' : form }, RequestContext(request))
        except TemplateDoesNotExist:
            raise Http404() 





def members_list(request):
    return list_detail.object_list(request, queryset=MemberProfile.objects.all())

def member_profile(request, username):
    user = User.objects.get(username=username)
    member = MemberProfile.objects.get(user=user.id)
    return direct_to_template(request, template="poly_assoc_website/memberprofile_detail.html", extra_context={'object' : member})


@login_required
@user_passes_test(lambda u: u.has_perm('cmsplugin_advancednews.add_news'))
def add_news(request):    
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        from django.template.defaultfilters import slugify
        form = NewsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/news/add/complete/')
        else:
            form.error = "News did not validate. Maybe some field are missing"
            return render_to_response('poly_assoc_website/news_add.html', {'form' : form }, RequestContext(request))
    if request.method == 'GET':        
        form = NewsForm()
        form.fields['content'] = ''
        try:
            return render_to_response('poly_assoc_website/news_add.html', {'form' : form,}, RequestContext(request))
        except TemplateDoesNotExist:
            raise Http404()

from cmsplugin_advancednews.models import News

@login_required
def my_items(request,user_pk):
    c = {}
    c.update(csrf(request))
    user = MemberProfile.objects.get(user=user_pk)
    if request.method == 'GET':
        my_photos = Photo.objects.filter(posted_by=user.pk)
        my_news = News.objects.filter(published_by=user.pk)
        my_pubs = Publication.objects.filter(author=user.pk)
        my_events = Event.objects.filter(posted_by=user.pk)
        my_links = UsefulLink.objects.filter(posted_by=user.pk)
        context = { 'my_photos' : my_photos,
                    'my_news' : my_news,
                    'my_publications' : my_pubs,
                    'my_events' : my_events,
                    'my_links' : my_links, }
        try:
            return render_to_response('poly_assoc_website/my_items.html', context, RequestContext(request))
        except TemplateDoesNotExist:
            raise Http404()
 
@login_required
@user_passes_test(lambda u: u.has_perm('cmsplugin_advancednews.change_news'))
def news_edit(request, news_id):
    c = {}
    c.update(csrf(request))
    news = News.objects.get(id=news_id)
    if request.method == 'GET':
        form = NewsForm(instance=news)
        try:
            return render_to_response('poly_assoc_website/news_edit.html', {'form' : form,}, RequestContext(request))
        except TemplateDoesNotExist:
            raise Http404()



@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.change_event'))
def event_edit(request, event_id):
    c = {}
    c.update(csrf(request))   
    event = Event.objects.get(id=event_id)
    user = event.posted_by
    if request.method == 'GET':       
        form = EventForm(instance=event)
        try:
            return render_to_response('poly_assoc_website/event_edit.html', {'form' : form,}, RequestContext(request))
        except TemplateDoesNotExist:
            raise Http404()
    if request.method == 'POST':
        form = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect('/my-items/%d/' % event.posted_by.id)
        else:
            form.error = "Event did not validate. Maybe some field are missing"
            return render_to_response('poly_assoc_website/event_edit.html', {'form' : form }, RequestContext(request))
   
@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.change_photo'))
def photo_edit(request, photo_id):
    c = {}
    c.update(csrf(request))   
    if request.method == 'GET':
        photo = Photo.objects.get(id=photo_id)
        form = PhotoForm(instance=photo)
        try:
            return render_to_response('poly_assoc_website/photo_edit.html',
                                      {'form' : form,
                                        'photo':photo}, 
                                      RequestContext(request))
        except TemplateDoesNotExist:
            raise Http404()
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = PhotoForm(request.POST,request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('/my-items/%d/' % photo.uploaded_by.id)
        else:
            form.error = "Photo did not validate. Maybe some field are missing"
            return render_to_response('poly_assoc_website/photo_edit.html', {'form' : form }, RequestContext(request))

@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.change_usefullink'))
def link_edit(request, link_id):
    c = {}
    c.update(csrf(request))   
    if request.method == 'GET':
        link = UsefulLink.objects.get(id=link_id)
        form = UsefulLinkForm(instance=link)
        try:
            return render_to_response('poly_assoc_website/usefullink_edit.html',
                                      {'form' : form}, 
                                      RequestContext(request))
        except TemplateDoesNotExist:
            raise Http404()
    if request.method == 'POST':
        link = UsefulLink.objects.get(id=link_id)
        form = UsefulLinkForm(request.POST,instance=link)
        if form.is_valid():
            form.save()
            return redirect('/my-items/%d/' % link.posted_by.id)
        else:
            form.error = "Useful link did not validate. Maybe some field are missing"
            return render_to_response('poly_assoc_website/usefullink_edit.html', {'form' : form }, RequestContext(request))

@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.change_publication'))
def publication_edit(request, pub_id):
    c = {}
    c.update(csrf(request))   
    if request.method == 'GET':
        publication = Publication.objects.get(id=pub_id)
        form = PublicationForm(instance=publication)
        try:
            return render_to_response('poly_assoc_website/publication_edit.html',
                                      {'form' : form}, 
                                      RequestContext(request))
        except TemplateDoesNotExist:
            raise Http404()
    if request.method == 'POST':
        publication = Publication.objects.get(id=pub_id)
        form = PublicationForm(request.POST,instance=publication)
        if form.is_valid():
            form.save()
            return redirect('/my-items/%d/' % publication.author.id)
        else:
            form.error = "Publication did not validate. Maybe some field are missing"
            return render_to_response('poly_assoc_website/publication_edit.html', {'form' : form }, RequestContext(request))

@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.delete_photo'))
def photo_delete(request, photo_id):
    c = {}
    c.update(csrf(request))    
    try:
        photo = Photo.objects.get(id=photo_id)
        photo.delete()
        return redirect('/my-items/%d/' % photo.uploaded_by.id)
    except ObjectDoesNotExist:
        raise Http404()

@login_required
@user_passes_test(lambda u: u.has_perm('cmsplugin_advancednews.delete_news'))
def news_delete(request, news_id):
    c = {}
    c.update(csrf(request))    
    try:
        news = News.objects.get(id=news_id)
        news.delete()
        return redirect('/my-items/%d/' % news.published_by.id)
    except ObjectDoesNotExist:
        raise Http404()


@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.delete_publication'))
def publication_delete(request, pub_id):
    c = {}
    c.update(csrf(request))    
    try:
        publication = Publication.objects.get(id=pub_id)
        publication.delete()
        return redirect('/my-items/%d/' % publication.author.id)
    except ObjectDoesNotExist:
        raise Http404()

@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.delete_event'))
def event_delete(request, event_id):
    c = {}
    c.update(csrf(request))    
    try:
        event = Event.objects.get(id=event_id)
        event.delete()
        return redirect('/my-items/%d/' % event.posted_by.id)
    except ObjectDoesNotExist:
        raise Http404()


@login_required
@user_passes_test(lambda u: u.has_perm('poly_assoc_website.delete_usefullink'))
def link_delete(request, link_id):
    c = {}
    c.update(csrf(request))    
    try:
        link = UsefulLink.objects.get(id=link_id)
        link.delete()
        return redirect('/my-items/%d/' % link.posted_by.id)
    except ObjectDoesNotExist:
        raise Http404()


