# -*- coding: utf-8 -*-
import os

gettext = lambda s: s

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
## BB NECESSARY
PROJECT_ROOT = PROJECT_DIR

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

LANGUAGES = [('en', 'en')]
DEFAULT_LANGUAGE = 0

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR,'polyassocdb.db'),
      
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0r6%7gip5tmez*vygfv+u14h@4lbt^8e2^26o#5_f_#b7%cm)u'


ALLOWED_INCLUDE_ROOTS = (os.path.join(PROJECT_DIR,'templates/poly_assoc_website/'))


# Email Settings
EMAIL_FILE_PATH = MEDIA_URL + 'emails/'
EMAIL_SUBJECT_PREFIX = '[PolyAsoociationAdmin]'
SERVER_EMAIL = 'no_reply@polyassoc.sci'
SEND_BROKEN_LINK_EMAILS = True


AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PROFILE_MODULE = 'poly_assoc_website.MemberProfile'

ANONYMOUS_USER_ID = -1


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
    #'djangobb_forum.middleware.LastLoginMiddleware',
    #'djangobb_forum.middleware.UsersOnline',
   
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    #'django_authopenid.context_processors.authopenid',
    #'djangobb_forum.context_processors.forum_settings',
    'poly_assoc_website.context_processors.latest_links',
    'poly_assoc_website.context_processors.latest_events',
    'poly_assoc_website.context_processors.latest_photos',
    'multilingual.context_processors.multilingual',
)



CMS_TEMPLATES = (
    ('cms.html', 'Neutral Page'),
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

#DJANGOBB_SRC = os.path.join(PROJECT_DIR,'./djangobb/')

LANGUAGES = (
    ('en', gettext('English')),
    ('pt-BR', gettext("Brazil")),
    ('fr', gettext('French')),
    ('sp', gettext('Spanish')),
    ('de', gettext('German')),
    
    
)

CMS_SOFTROOT = os.path.join(PROJECT_DIR, '/cms/')
CMS_MEDIA_ROOT = os.path.join(PROJECT_DIR, '/media/cms/')
CMS_MEDIA_URL = '/media/cms/'
#CMS_LANGUAGES = {1:['en','fr','de','pt-BR'],}

CMS_APPLICATIONS_URLS = (
    ('cmsplugin_advancednews.urls', 'News'),
)
CMS_NAVIGATION_EXTENDERS = (
    ('cmsplugin_advancednews.navigation.get_nodes','News navigation'),
)

CMS_MODERATOR = False
CMS_PERMISSION = False
CMS_SHOW_START_DATE = False
CMS_SHOW_END_DATE = False
CMS_SEO_FIELDS = False
CMS_URL_OVERWRITE = False
CMS_REDIRECTS = False
CMS_APPHOOKS = ()
CMS_MENU_TITLE_OVERWRITE = ''

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admin',
    'cms',
    'menus',
    'mptt',
    'appmedia',
    'south',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    #'cms.plugins.snippet',
    #'cms.plugins.googlemap',
    #'registration',
    #'django_authopenid',
    #'djangobb_forum',
    'haystack',
    #'messages',
    'userena',
    'guardian',
    'easy_thumbnails',
    'poly_assoc_website',
    'cmsplugin_advancednews',
)

try:
    import mailer
    INSTALLED_APPS += ('mailer',)
    EMAIL_BACKEND = "mailer.backend.DbBackend"
except ImportError:
    pass






# Haystack settings
HAYSTACK_SITECONF = 'search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_ROOT, 'search_index')

# Account settings
ACCOUNT_ACTIVATION_DAYS = 10
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

# easy_thumbnails settings

THUMBNAIL_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'thumbs')
THUMBNAIL_MEDIA_URL = MEDIA_URL + 'thumbs/'

#Cache settings1    
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

try:
    from local_settings import *
except ImportError:
    pass
