from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^scene/', include('lassie.scene.urls'), name='scene'),
    url(r'^admin/', include(admin.site.urls)),
)
