from poly_assoc_website.models import UsefulLink, Event, Photo

import datetime
from haystack.query import EmptySearchQuerySet
from django.core.paginator import Paginator, InvalidPage
from haystack.forms import ModelSearchForm, FacetedSearchForm

def search_form(request, form_class=ModelSearchForm, load_all=True, searchqueryset=None):
    query = ''
    results = EmptySearchQuerySet()
    
    if request.GET.get('q'):
        form = form_class(request.GET, searchqueryset=searchqueryset, load_all=load_all)
        
        if form.is_valid():
            query = form.cleaned_data['q']
            results = form.search()
    else:
        form = form_class(searchqueryset=searchqueryset, load_all=load_all)
       
    context = {
        'search_form': form,
        'sq': query,
        'search_suggestion': None,
    }

    return context

def latest_links(request, queryset=UsefulLink.objects.all(), date_field='pub_datetime', num_latest=4,
            extra_context=None, allow_future=False, 
            template_object_name='latest_links'):
    
    """
    Generic top-level archive of date-based objects.

    Templates: ``<app_label>/<model_name>_archive.html``
    Context:
        date_list
            List of years
        latest
            Latest N (defaults to 15) objects by date
    """    
    
    if extra_context is None: extra_context = {}
    
    if not allow_future:
        queryset = queryset.filter(**{'%s__lte' % date_field: datetime.datetime.now()})
    date_list = queryset.dates(date_field, 'year')[::-1]
    
    if date_list and num_latest:
        latest = queryset.order_by('-'+date_field)[:num_latest]
    else:
        latest = None

    
    return { template_object_name : latest, 'date_list' : date_list,
             'total_links' : queryset.count()   }

def latest_events(request, queryset=Event.objects.all(), date_field='pub_datetime',
                extra_context=None, allow_future=True, num_latest=5, template_object_name='latest_events',):
    """
    Generic top-level archive of date-based objects.

    Templates: ``<app_label>/<model_name>_archive.html``
    Context:
        date_list
            List of years
        latest
            Latest N (defaults to 15) objects by date
    """    
    
    if extra_context is None: extra_context = {}
    
    if not allow_future:
        queryset = queryset.filter(**{'%s__lte' % date_field: datetime.datetime.now()})
    date_list = queryset.dates(date_field, 'year')[::-1]
    
    if date_list and num_latest:
        latest = queryset.order_by('-'+date_field)[:num_latest]
    else:
        latest = None

    
    return { template_object_name : latest, 'date_list' : date_list,
             'total_events' : queryset.count()}


def latest_photos(request, queryset=Photo.objects.all(), date_field='pub_datetime',
                extra_context=None, allow_future=True, num_latest=9, template_object_name='latest_photos',):
    """
    Generic top-level archive of date-based objects.

    Templates: ``<app_label>/<model_name>_archive.html``
    Context:
        date_list
            List of years
        latest
            Latest N (defaults to 15) objects by date
    """    
    
    if extra_context is None: extra_context = {}
    
    if not allow_future:
        queryset = queryset.filter(**{'%s__lte' % date_field: datetime.datetime.now()})
    date_list = queryset.dates(date_field, 'year')[::-1]
    
    if date_list and num_latest:
        latest = queryset.order_by('-'+date_field)[:num_latest]
    else:
        latest = None

    
    return { template_object_name : latest, 'date_list' : date_list,
             'total_events' : queryset.count()}
