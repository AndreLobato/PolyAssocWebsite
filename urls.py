from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic.list_detail import object_list
from django.views.generic.simple import direct_to_template, redirect_to

from poly_assoc_website.views import *
from poly_assoc_website.models import Event

#from sitemap import SitemapForum, SitemapTopic
#from forms import RegistrationFormUtfUsername
#from djangobb_forum import settings as forum_settings

# HACK for add default_params with RegistrationFormUtfUsername and backend to registration urlpattern
# Must be changed after django-authopenid #50 (signup-page-does-not-work-whih-django-registration)
# will be fixed
'''from django_authopenid.urls import urlpatterns as authopenid_urlpatterns
for i, rurl in enumerate(authopenid_urlpatterns):
    if rurl.name == 'registration_register':
        authopenid_urlpatterns[i].default_args.update({'form_class': RegistrationFormUtfUsername})'''
# 'backend': 'registration.backends.default.DefaultBackend'})
# elif rurl.name == 'registration_activate':
# authopenid_urlpatterns[i].default_args = {'backend': 'registration.backends.default.DefaultBackend'}

admin.autodiscover()

'''
sitemaps = {
   
    'topic': SitemapTopic,
}'''


urlpatterns = patterns('',

    # Site base
    url(r'^$', redirect_to, {'url':'/cms/latest-news'}),

    # CMS
    url(r'^cms/', include('cms.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    (r'^news/add/complete', direct_to_template, {'template':"poly_assoc_website/news_add_complete.html"}),

    url(r'^news/', include('cmsplugin_advancednews.urls')),

    url(r'^news/(?P<news_id>\d+)/edit/', news_edit, name="news_edit"),
    url(r'^news/(?P<news_id>\d+)/delete/', news_delete, name="news_delete"),
    url(r'^news/add/', add_news, name="add_news"),
    
    #Haystack
    
    (r'^search/', include('haystack.urls')),

    # Sitemap
    #(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Forum Apps
    #(r'^forum/account/', include(authopenid_urlpatterns)),
    #(r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),

   
    # Userena
    url(r'^accounts/', include('userena.urls')),
    (r'^accounts/logout$', signout),

    # Polychaetologists Association Website

   (r'^my-items/(?P<user_pk>\d+)/', my_items),
    #url(r'^my_item/(P<item_class>\w+)/(?P<item_id>\d+)/', my_item_delete, name="my_item_delete"),

    url(r'^news/add/', add_news),
    (r'^useful-links/', useful_links),
    url(r'^new-link/', new_useful_link, name="add_link"),
    url(r'^useful-link/(?P<link_id>\d+)/edit/', link_edit, name="link_edit"),
    url(r'^useful-link/(?P<link_id>\d+)/delete/', link_delete, name="link_delete"),

    (r'^latest-links/', latest_links),

    url(r'^event/add/$', add_event, name="add_event"),
    (r'^event/add/complete/', direct_to_template,{'template':"poly_assoc_website/event_add_complete.html"}),
    url(r'^event/$', event_detail, name="event_detail"),
    url(r'^event/(?P<event_id>\d+)/edit/', event_edit, name="event_edit"),
    url(r'^event/(?P<event_id>\d+)/delete/', event_delete, name="event_delete"),

    (r'^events/', show_all_events),



    (r'^publications/$', publications),
    (r'^publications/%(username)s/', my_publications),
    url(r'^publication/add/$', add_publication, name="add_publication"),
    (r'^publication/add/complete/$', direct_to_template, {'template' : 'poly_assoc_website/publication_add_complete.html'}),
    url(r'^publication/(?P<pub_id>\d+)/edit/', publication_edit, name="publication_edit"),
    url(r'^publication/(?P<pub_id>\d+)/delete/', publication_delete, name="publication_delete"),
    url(r'^publication/(?P<pub_id>\d+)/$', publication_detail, name="publication_detail"),
    
    (r'^photos/$', photo_gallery),
    (r'^photos/(\w+)$', photo_gallery),
    url(r'^photos/add/$', add_photo, name="add_photo"),
    (r'^photos/add/complete/$', direct_to_template, {'template' : "poly_assoc_website/photo_add_complete.html"}),
    url(r'^photo/(?P<photo_id>\d+)/edit/$', photo_edit, name="photo_edit"),
    url(r'^photo/(?P<photo_id>\d+)/delete/$', photo_delete, name="photo_delete"),

    (r'^members/$', members_list),
    url(r'^members/(\w+)/$', member_profile, name="member_profile"),
)

'''if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^forum/pm/', include('messages.urls')),
   )'''


if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    )
    # staticfiles
    #urlpatterns += staticfiles_urlpatterns()



