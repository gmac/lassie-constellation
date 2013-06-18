import dj_database_url
from lassie.settings.base import *

DEBUG = True
SERVE_STATIC = True
SERVE_MEDIA = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.config(),
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')