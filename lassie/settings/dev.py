import dj_database_url
from .base import *

DEBUG = True
SERVE_STATIC = True
SERVE_MEDIA = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.config(),
}