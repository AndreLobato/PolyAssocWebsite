from haystack.indexes import *
from haystack import site
from cms.models import Page, Title
from integration.models import MemberProfile 



class PageIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    created_by = models.CharField(model_attr='user')
    publication_date = models.DateTimeField(model_attr='publication_date')
    

class TitleIndex(SearchIndex):
    text = models.CharField(document=True, use_template=True)
    title = models.Charfield(model_attr='title')
    slug = models.Slugfield(model_attr='slug')
    meta_keywords = models.Charfield(model_attr='meta_keywords')


site.register(Page, PageIndex)
site.register(TitlePage, TitleIndex)
