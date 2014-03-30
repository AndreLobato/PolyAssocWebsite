from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class NewsApphook(CMSApp):
    name = _("Latest Advanced News")
    urls = ["cmsplugin_advancednews.urls"]

apphook_pool.register(NewsApphook)
