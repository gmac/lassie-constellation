from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.resources import ModelResource
from lassie.scene.models import Scene, Layer, Grid, Matrix


# API Resources

class SceneResource(ModelResource):
    class Meta:
        queryset = Scene.objects.all()
        resource_name = 'scene'
        filtering = {
            'id': ALL,
        }
        

class LayerResource(ModelResource):
    scene = fields.ForeignKey(SceneResource, 'scene')
    
    class Meta:
        queryset = Layer.objects.all()
        resource_name = 'layer'
        always_return_data = True
        authorization = Authorization()
        filtering = {
            'scene': ALL_WITH_RELATIONS,
        }

            
class GridResource(ModelResource):
    scene = fields.ForeignKey(SceneResource, 'scene')

    class Meta:
        queryset = Grid.objects.all()
        resource_name = 'grid'
        always_return_data = True
        authorization = Authorization()
        filtering = {
            'scene': ALL_WITH_RELATIONS,
        }

            
class MatrixResource(ModelResource):
    scene = fields.ForeignKey(SceneResource, 'scene')

    class Meta:
        queryset = Matrix.objects.all()
        resource_name = 'matrix'
        always_return_data = True
        authorization = Authorization()
        filtering = {
            'scene': ALL_WITH_RELATIONS,
        }

