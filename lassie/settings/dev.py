import dj_database_url
from lassie.settings.base import *

DEBUG = True
SERVE_STATIC = True
SERVE_MEDIA = True
TEMPLATE_DEBUG = DEBUG

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


DATABASE_URL = 'postgres://localhost/lassie'

DATABASES = {
    'default': dj_database_url.config(),
}