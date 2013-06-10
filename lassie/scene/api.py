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
        excludes = ['']
        resource_name = 'scene'
        authorization = Authorization()
        

class SceneObjectResource(ModelResource):
    #scene = fields.ForeignKey(SceneResource, 'scene')
    
    class Meta:
        queryset = SceneObject.objects.all()
        resource_name = 'object'
        authorization = Authorization()

    def get_object_list(self, request):
        obj_list = super(SceneObjectResource, self).get_object_list(request)
        return obj_list.filter(scene=request.GET['scene']).order_by('depth')
            

# API structure

v1_api = Api(api_name='v1')
v1_api.register(SceneResource())
v1_api.register(SceneObjectResource())