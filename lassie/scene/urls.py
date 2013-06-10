from django.conf.urls import patterns, include, url
from lassie.scene import views
from lassie.scene.api import v1_api

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
	url(r'^$', views.scene_index, name='index'),
	url(r'^(?P<scene_id>\d+)/$', views.scene_edit, name='edit'),
)
