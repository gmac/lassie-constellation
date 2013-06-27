from django.conf.urls import patterns, include, url
from lassie.scene import views

urlpatterns = patterns('',
	url(r'^(?P<scene_id>\d+)/layout/$', views.scene_edit, name='edit'),
)