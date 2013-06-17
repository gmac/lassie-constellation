from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from lassie.api import v1_api

admin.autodiscover()

# URL Patterns

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^scene/', include('lassie.scene.urls'), name='scene'),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.SERVE_STATIC:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
    )