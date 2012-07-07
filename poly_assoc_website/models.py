from django.db import models
from django.contrib.auth.models import User

from userena.models import UserenaLanguageBaseProfile




class MemberProfile(UserenaLanguageBaseProfile):
    about_me = models.TextField(blank=True)
    institution = models.CharField(max_length=200, help_text="Name of the place where you work at.")
    work_location = models.CharField(max_length=200, help_text="City and country where your institution is located.")
    research_area = models.CharField(max_length=200)
    homepage_url =  models.URLField(blank=True,verify_exists=True)
    curriculum_url = models.URLField(blank=True,verify_exists=True)
    pub_datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def get_absolute_url(self):
        return '/accounts/%s/' % self.user.username

    def __unicode__(self):
        return '%s' % self.user.username





class Publication(models.Model):
    author = models.CharField(max_length=128, help_text="Please, use scientific names only. e.g. STUART, E.P.")
    others_authors = models.CharField(max_length=256, blank=True, help_text="Same as above, use dot-comma as separator")
    title = models.CharField(max_length=200, help_text="Full title of your article.")
    abstract = models.TextField(blank=True)    
    publisher = models.CharField(max_length=256, help_text="Name of this publication publisher")
    publish_date = models.DateField(help_text="Date when document it was published")   
    url = models.URLField(help_text="URL to publication online", blank=True)    
    posted_by = models.ForeignKey(MemberProfile)
    pub_datetime = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/publication/%i/" % self.id

    def __unicode__(self):
        return self.author + ' ' + str(self.publish_date.year) + '. ' + self.title

class Event(models.Model):
    EVENT_CHOICES = (('Meeting','Meeting'),('Congress','Congress'),('Simposium','Simposium'),
                    ('Forum','Forum'))
    event_type = models.CharField(max_length=10, choices=EVENT_CHOICES)
    title = models.CharField(max_length=200)
    event_datetime = models.DateTimeField()
    location = models.TextField()
    url = models.URLField(verify_exists=True)
    details = models.TextField(blank=True)
    posted_by = models.ForeignKey(MemberProfile)
    pub_datetime = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return '/event/?event_id=%i' % self.id

    def __unicode__(self):
        return '%s' % self.title
        
    

class UsefulLink(models.Model):
    url = models.URLField(verify_exists=False)
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(MemberProfile,                                                 
                                related_name='name')
    pub_datetime = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return '/useful-links/'

    def __unicode__(self):
        return '%s' % self.url


class Photo(models.Model):
    title = models.CharField(max_length=128)
    slug_title = models.CharField(max_length=128, help_text="Unique character set identifier for this image")
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)
    pub_datetime = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(MemberProfile)

    def get_absolute_url(self):
        return '/photos/#%s' % self.slug_title
    
    def __unicode__(self):
        return '%s' % self.title



