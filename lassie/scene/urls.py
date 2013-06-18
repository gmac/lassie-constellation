from django.conf.urls import patterns, include, url
from lassie.scene import views

urlpatterns = patterns('',
	url(r'^$', views.scene_index, name='index'),
	url(r'^(?P<scene_id>\d+)/$', views.scene_edit, name='edit'),
	url(r'^layer/(?P<layer_id>\d+)/$', views.scene_layer, name='layer'),
)