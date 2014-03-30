from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_advancednews.models import LatestAdvancedNewsPlugin, News
from cmsplugin_advancednews import settings

from django.conf import settings

class CMSLatestAdvancedNewsPlugin(CMSPluginBase):
    """ Plugin class for the latest news """
    model = LatestAdvancedNewsPlugin

    name = _('Latest news')
    render_template = 'cmsplugin_advancednews/latest_news.html'
    
    
    def render(self, context, instance, placeholder):
        """ Render the latest news """
        query = News.published
        if instance.category is None:
            latest = query.all()[:instance.limit]
        else:
            latest = query.filter(category=instance.category).all()[:instance.limit]
        context.update({
            'instance': instance,
            'latest': latest,
            'placeholder': placeholder,
        })
        return context

##if not settings.DISABLE_LATEST_ADVANCEDNEWS_PLUGIN:
plugin_pool.register_plugin(CMSLatestAdvancedNewsPlugin)
