from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import redirect_to
from django.views.generic.list_detail import object_list
from django.views.generic.simple import direct_to_template

from sitemap import SitemapForum, SitemapTopic
from forms import RegistrationFormUtfUsername
from djangobb_forum import settings as forum_settings

from poly_assoc_website.views import *
from poly_assoc_website.models import Event

# HACK for add default_params with RegistrationFormUtfUsername and backend to registration urlpattern
# Must be changed after django-authopenid #50 (signup-page-does-not-work-whih-django-registration)
# will be fixed
from django_authopenid.urls import urlpatterns as authopenid_urlpatterns
for i, rurl in enumerate(authopenid_urlpatterns):
    if rurl.name == 'registration_register':
        authopenid_urlpatterns[i].default_args.update({'form_class': RegistrationFormUtfUsername})
#                                                  'backend': 'registration.backends.default.DefaultBackend'})
#    elif rurl.name == 'registration_activate':
#                authopenid_urlpatterns[i].default_args = {'backend': 'registration.backends.default.DefaultBackend'}

admin.autodiscover()


sitemaps = {
    'forum': SitemapForum,
    'topic': SitemapTopic,
}


urlpatterns = patterns('',

    # Site base
    url(r'^$', load_base_page),
    
    # Admin    
    url(r'^admin/', include(admin.site.urls)),
    
    # CMS
    url(r'^cms/', include('cms.urls')),

    #Haystack
    
    (r'^search/', include('haystack.urls')),

    # Sitemap
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    
    # Apps
    (r'^forum/account/', include(authopenid_urlpatterns)),

    (r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),
    
    # Userena 
    (r'^accounts/', include('userena.urls')),

    # Polychaetologists Association Website
    (r'^useful-links/', useful_links),
    (r'^new-link/', new_useful_link),
    (r'^latest-links/', latest_links),
    (r'^event/add', add_event),
    (r'^event/add/complete/', direct_to_template, "poly_assoc_website/event_add_complete.html"),
    (r'^event/?event_id=(\d+)$', event_detail),
    (r'^events/', show_all_events),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns





# PM Extension
if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^forum/pm/', include('messages.urls')),
   )

if (settings.DEBUG):
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
