from django.conf import settings as django_settings

# Uses CKEditor as editor (no inline plugins). Requires ckeditor app. 
USE_CKEDITOR = getattr(django_settings, 'CMS_USE_CKEDITOR', "ckeditor" in django_settings.INSTALLED_APPS)

DISABLE_LATEST_NEWS_PLUGIN = getattr(django_settings, 'CMSPLUGIN_NEWS_DISABLE_LATEST_NEWS_PLUGIN', False)
