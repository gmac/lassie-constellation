from tastypie import fields
from tastypie.api import Api
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.resources import ModelResource
from lassie.scene.models import Scene, SceneObject


# API Resources

class SceneResource(ModelResource):
    class Meta:
        queryset = Scene.objects.all()
        resource_name = 'scene'
        filtering = {
            'id': ALL,
        }
        

class SceneObjectResource(ModelResource):
    scene = fields.ForeignKey(SceneResource, 'scene')
    
    class Meta:
        queryset = SceneObject.objects.all()
        resource_name = 'object'
        always_return_data = True
        authorization = Authorization()
        filtering = {
            'scene': ALL_WITH_RELATIONS,
        }
            

# API structure

v1_api = Api(api_name='v1')
v1_api.register(SceneResource())
v1_api.register(SceneObjectResource())