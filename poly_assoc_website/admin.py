from django.contrib import admin

from poly_assoc_website.models import UsefulLink, Publication, Event, Photo


admin.site.register(UsefulLink)
admin.site.register(Event)
admin.site.register(Publication)
admin.site.register(Photo)
