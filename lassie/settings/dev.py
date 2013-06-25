from lassie.settings.base import *

DEBUG = True
SERVE_STATIC = True
SERVE_MEDIA = True
TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = ''

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# This function is used to determine when the debug toolbar should be
# displayed: when the user is logged in and not in the admin.
def _ddt_check(request):
    if request.path.startswith("/admin/"):
        return False
    if request.user.is_authenticated():
        return True
    return False


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': _ddt_check
}


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': os.path.join(PROJECT_DIR, 'lassie_db'), # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lassie',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}
