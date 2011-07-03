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
    
    def __unicode__(self):
        return '%s' % self.user.username



class Publication(models.Model):
    author = models.ForeignKey(MemberProfile)
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    publisher = models.CharField(max_length=200)
    publish_date = models.DateField("Date wich paper was published", blank=True)   
    url = models.URLField("Link to publication online",blank=True,verify_exists=False)    
    pub_datetime = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    EVENT_CHOICES = (('Meeting','Meeting'),('Congress','Congress'),('Simposium','Simposium'),
                    ('Forum','Forum'))
    event_type = models.CharField(max_length=10, choices=EVENT_CHOICES)
    title = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField()
    location = models.TextField()
    url = models.URLField(blank=True,verify_exists=False)
    details = models.TextField(blank=True)
    posted_by = models.ForeignKey(MemberProfile)
    pub_datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.title
        
    

class UsefulLink(models.Model):
    url = models.URLField(verify_exists=False)
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(MemberProfile,                                                 
                                related_name='name')
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s' % self.url


class Photo(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)
    pub_datetime = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(MemberProfile)
    
    def __unicode__(self):
        return '%s' % self.name



