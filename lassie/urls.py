from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from lassie.scene.api import SceneResource, LayerResource, GridResource, MatrixResource

admin.autodiscover()

# API structure

v1_api = Api(api_name='v1')
v1_api.register(SceneResource())
v1_api.register(LayerResource())
v1_api.register(GridResource())
v1_api.register(MatrixResource())

# URL Patterns

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
	url(r'^scene/', include('lassie.scene.urls'), name='scene'),
    url(r'^admin/', include(admin.site.urls)),
)
