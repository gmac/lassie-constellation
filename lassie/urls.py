from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from lassie.api import v1_api
from lassie.views import site_index, test_page

admin.autodiscover()

# URL Patterns

urlpatterns = patterns('',
    url(r'^$', site_index, name='home'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^scene/', include('lassie.scene.urls'), name='scene'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', test_page, name='test_page'),
)


if settings.SERVE_STATIC:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True
        }),
    )
    
if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
    )