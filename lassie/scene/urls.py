from django.conf.urls import patterns, include, url
from lassie.scene import views
from lassie.scene.api import v1_api

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^api/', include(v1_api.urls)),
	url(r'^(?P<scene_id>\d+)/$', views.get_scene, name='scene'),
	url(r'^(?P<scene_id>\d+)/object/$', views.get_all_objects, name='scene_object_all'),
	url(r'^(?P<scene_id>\d+)/object/(?P<object_id>\d+)/$', views.get_object, name='scene_object'),
)
